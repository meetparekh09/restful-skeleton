"""
    Module for Unit Testing service.server.py file
"""

import unittest
from service import app
from flask_api import status

class TestServer(unittest.TestCase):
    """ Server Test """


    def setUp(self):
        """ Runs before each test """
        self.app = app.test_client()


    def tearDown(self):
        """ Runs after each test """
        pass

    def setUpClass(self):
        """ Runs before any test in class runs """
        pass

    def tearDownClass(self):
        """ Runs after all test in class runs """
        pass

    def test_index(self):
        """ Test whether server responds on index page """
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
