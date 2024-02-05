#!/usr/bin/python3

"""
This module defines the views for State objects in the API
"""

from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from models import storage
from models.state import State


@app_views.route('/states', method=['GET'], strict_slashes=FALSE)
def get_states():
    """Retrieve the list of all State objects"""
    states = storage.all(State).values()
    return jsonify([state.to_dict for state in states])


@app_views.route('/states/<state_id>', method=['GET'], strict_slashes=FALSE)
def get_state(state_id):
    """Retrieve a State object by ID"""
    state = storage.get(State, state_id)
    if state in None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', method=['DELETE'], strict_slashes=FALSE)
def delete_state(state_id):
    """Delete a State object by ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', method=['POST'], strict_slashes=FALSE)
def create_state():
    """Create a new State"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', method=['PUT'], strict_slashes=FALSE)
def update_state(state_id):
    """Update a State object by ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
