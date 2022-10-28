#!/usr/bin/python3
"""index of the application
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def Index():
    """route to the status
    """
    return jsonify({"status": "OK"})