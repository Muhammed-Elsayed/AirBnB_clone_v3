#!/usr/bin/python3
"""
View for Cities that handles all RESTful API actions
"""

from flask import jsonify, request, abort, make_response
from models import storage
from models.state import State
from models.city import City
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """ get city objects related to a state """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities_list = []
    for city_obj in state.cities:
        cities_list.append(city_obj.to_dict())
    return jsonify(cities_list)


@app_views.route('/cities/<city_id>', method=['GET'],
                 strict_slashes=False)
def get_city_By_ID(city_id):
    """get a city object by id"""
    city_obj = storage.get(City, city_id)
    if city_obj is None:
        abort(404)
    return (jsonify(city_obj.to_dict()))


@app_views.route('/cities/<city_id>', method='DELETE',
                 strict_slashes=False)
def delete_city_by_ID(city_id):
    """delete city obj by id"""
    city_obj = storage.get(City, city_id)
    if (city_obj is None):
        abort(400)
    city_obj.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/states/<state_id>/cities', method='POST',
                 strict_slashes=False)
def add_new_cityObj(state_id):
    """add new city obj"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)

    js = request.get_json()
    obj = City(**js)
    obj.state_id = state.id
    obj.save()
    return jsonify(obj.to_dict()), 201


@app_views.route('/cities/<string:city_id>', methods=['PUT'],
                 strict_slashes=False)
def post_city(city_id):
    """  """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(City, city_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict())
