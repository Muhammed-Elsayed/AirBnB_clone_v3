#!/usr/bin/python3
""" states.py that handles all default RestFul API actions"""

from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from flask import abort, request, jsonify
import json


@app_views.route("/states/<state_id>/cities")
def get_cities(state_id):
    """ get cities"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify([city.to_dict() for city in state.cities])


@app_views.route("/cities/<city_id>")
def get_city(city_id):
    """ get city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route("/states/<state_id>/cities", methods=['DELETE'])
def delete_city(city_id):
    """ delete city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    city.delete()
    storage.save()
    return jsonify({}), 200

#--Todo: Not stable yet wish you luck with it bero
@app_views.route("/states/<state_id>/cities", methods=['POST'])
def post_city(state_id):
    """ post city"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    try:
        request_data = request.get_json()
    except Exception:
        return jsonify('Not a JSON'), 400
    if 'name' not in request_data:
        return jsonify('Missing name'), 400

    new_city = City(**request_data)
    storage.new(new_city)
    storage.save()

    return jsonify(new_city.to_dict()), 201