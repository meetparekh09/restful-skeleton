"""
    Module for RESTful API
"""

from flask import jsonify, make_response
from flask_api import status

from . import app


@app.route('/')
def index():
    """ Root URL Response """
    return make_response(jsonify(name='Demo REST API Service',
                   version='1.0',
                  ), status.HTTP_200_OK)
