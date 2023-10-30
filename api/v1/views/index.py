#!/usr/bin/python3
"""returns a status of api"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """returns the status of the api"""
    if request.method == 'GET':
        return jsonify({"status": "ok"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """retrieves the num of each objs based on a type"""
    if request.method == 'GET':
        stats = {}
        classes = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in classes.items():
            stats[value] = storage.count(key)
        return jsonify(stats)
