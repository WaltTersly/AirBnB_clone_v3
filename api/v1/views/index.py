#!/usr/bin/python3
"""index of the application
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """route to the status
    """
    return jsonify({"status": "OK"})
