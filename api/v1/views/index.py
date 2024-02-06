#!/usr/bin/python3

from flask import jsonify
from . import app_views
from models import storage

""" Define a route /status on the app_views Blueprint """


@app_views.route('/status', methods=['GET'])
def status_ok():
    """ returns  json message with status OK"""
    return jsonify({"status": "OK"}), 200


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    Endpoint to retrieve the number of each object type

    Returns:
        JSON response with the count of each object type
    """
    stats_dict = {}
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]

    for cls_name in classes:
        count = storage.count(cls_name)
        stats_dict[cls_name] = count

    return jsonify(stats_dict)
