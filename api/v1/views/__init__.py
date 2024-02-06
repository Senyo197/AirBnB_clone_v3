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

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
