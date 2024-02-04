#!/usr/bin/python3

from flask import jsonify
from api.v1/views import app_views


# Define a route /status on the app_views Blueprint
@app_views.route('/status', methods=['GET'])
def status():
    """
    Endpoint to get the status of the API.

    Returns:
        JSON response with the status: "OK".
    """
    jsonify({"status": "OK"})
