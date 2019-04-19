"""
    Module for RESTful API
"""

from flask import jsonify
from flask_api import status

from . import app


@app.route('/')
def index():
    """ Root URL Response """
    return jsonify(name='Demo REST API Service',
                   version='1.0',
                  ), status.HTTP_200_OK
