"""
Package: app

Package for the application models and services
This module also sets up the logging to be used with gunicorn
"""
import os
import sys
import logging
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
app.config['LOGGING_LEVEL'] = logging.INFO

# Set up Gunicorn Loggers
print 'Setting up logging for {}...'.format(__name__)
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    if gunicorn_logger:
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

app.logger.info('************************************************************')
app.logger.info('        I N V E N T O R Y   R E S T   A P I   S E R V I C E ')
app.logger.info('************************************************************')
app.logger.info('Logging established')


import server
