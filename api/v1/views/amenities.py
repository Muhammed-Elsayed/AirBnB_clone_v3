#!/usr/bin/python3
"""view for amenities using rest apis"""

from models import storage
from models.amenity import Amenity
from flask import abort, request, jsonify, make_response
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'])
def get_all_amenites_objs():
    """ get amenities """
    all_amenities = storage.all(Amenity).values()
    list_amenities = []
    for amenity in all_amenities:
        list_amenities.append(amenity.to_dict())
    return jsonify(list_amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """ get amenity object by it's id """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)

    return (jsonify(amenity.to_dict()))


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """delete amenity obj by it's ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        storage.delete(amenity)
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route('/amenities', methods=['POST'])
def post_amenity():
    """ Create amenity """
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')

    if data.get('name', None):
        amenity = Amenity(**data)
        amenity.save()
        return jsonify(amenity.to_dict()), 201
    else:
        abort(400, 'Missing name')


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def put_amenity(amenity_id):
    """ Updates amenity obj by id """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    ignore_keys = ['id', 'created_at', 'updated_at']
    for k, v in data.items():
        if k not in ignore_keys:
            setattr(amenity, k, v)
    amenity.save()
    return jsonify(amenity.to_dict())
