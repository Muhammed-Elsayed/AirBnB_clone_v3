#!/usr/bin/python3
"""returns a status of api"""
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/status', methods=['GET'])
def status():
    """returns the status of the api"""
    if request.method == 'GET':
        return jsonify({"status": "ok"})
