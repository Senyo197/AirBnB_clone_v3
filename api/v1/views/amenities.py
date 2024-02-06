#!/usr/bin/python3

"""
This module defines ithe views for amenity objects in the API
"""

from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from models import storage
from models.amenities import Amenity


@app_views.route('/amenities', method=['GET'], strict_slashes=FALSE)
def get_amenities():
    """Retrieve the list of all Amenity objects"""
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict for amenity in amenities])


@app_views.route('/amenities/<amenity_id>', method=['GET'],
                 strict_slashes=FALSE)
def get_amenity(amenity_id):
    """Retrieve a Amenity object by ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity in None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', method=['DELETE'],
                 strict_slashes=FALSE)
def delete_amenity(amenity_id):
    """Delete a Amenity object by ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', method=['POST'], strict_slashes=FALSE)
def create_amenity():
    """Create a new amenity"""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")
    new_amenity = Amenity(**data)
    storage.new(new_amenity)
    storage.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', method=['PUT'],
                 strict_slashes=FALSE)
def update_amenity(amenity_id):
    """Update a Amenity object by ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
