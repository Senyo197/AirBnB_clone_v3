#!/usr/bin/python3
"""
This module initializes the views for the API version 1.

It creates a Flask Blueprint named app_views with a URL prefix of /api/v1
Additionally, it performs a wildcard import of names from the
api.v1.views.index module

Note: PEP8 may complain about wildcard imports, but it's intentional in this
context.
"""

from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='api/v1')
