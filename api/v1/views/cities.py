#!/usr/bin/python3
"""view for cities using rest apis"""

from models import storage
from models.state import State
from models.city import City
from flask import abort, request, jsonify, make_response
from api.v1.views import app_views
import json


@app_views.route("/states/<state_id>/cities", methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """ get cities"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify([city.to_dict() for city in state.cities])


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city_by_id(city_id):
    """get a city by ID"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city_byID(city_id):
    """delete a city by it's id"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({})


@app_views.route('/states/<string:state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_obj_city(state_id):
    """Create a new city instance."""
    state = storage.get(State, state_id)

    if state is None:
        abort(404)

    request_data = request.get_json()

    if not request_data:
        return jsonify({"error": "Not a JSON"}), 400

    if 'name' not in request_data:
        return jsonify({"error": "Missing name"}), 400

    city_data = {'name': request_data['name'], 'state_id': state.id}
    city = City(**city_data)
    city.save()

    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'],
                 strict_slashes=False)
def updating_city_obj(city_id):
    """updating a city obj"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    for key, value in request.get_json().items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    storage.save()
    return jsonify(city.to_dict())
