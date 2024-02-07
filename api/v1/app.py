#!/usr/bin/python3

"""
Entry point for flask
"""

from api.v1.views import app_views
from flask_cors import CORS
from flask import Flask, jsonify
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)
""" Enable CORS for /* on 0.0.0.0 """
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(error):
    """
    Function to be called when the application context is torn down
    It closes the database connection using storage.close()
    """
    storage.close()


@app.errorhandler(404)
def non_found(error):
    """
    Custom 404 error handler that returns a JSON-formatted 404 response
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    import os
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
