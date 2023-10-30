
#!/usr/bin/python3
"""
View for amenities 
"""

from flask import jsonify, request, abort, make_response
from models import storage
from models.state import Amenity
from api.v1.views import app_views


@app_views.route('/amenities', method = ['GET'],
				 strict_slashes=False)
def get_all_amenity_obj():
	"""get all amenity obj"""
	amenity_objs_list = []
	for amenity_obj in storage.all(Amenity).values():
		amenity_objs_list.append(amenity_obj.to_dict())

	return (jsonify(amenity_objs_list))






