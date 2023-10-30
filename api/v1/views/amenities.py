#!/usr/bin/python3
"""view for amenities using rest apis"""

from models import storage
from models.amenity import Amenity
from flask import abort, request, jsonify, make_response
from api.v1.views import app_views
import json

@app_views.route('/amenities', methods=['GET'],
				 strict_slashes=False)
def get_all_amenites_objs():
    """ get amenities by id """
    all_list = [obj.to_dict() for obj in storage.all(Amenity).values()]
    return jsonify(all_list)