#!/usr/bin/python3
"""starting an api"""
from flask import Flask, jsonify, make_response
from models import storage
import os
from api.v1.views import app_views
from werkzeug.exceptions import NotFound


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exc):
    """closing the current session"""
    storage.close()


@app.errorhandler(NotFound)
def not_found_error(error):
    response = {
        "error": "Not found"
    }
    return make_response(jsonify(response), 404)


if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
