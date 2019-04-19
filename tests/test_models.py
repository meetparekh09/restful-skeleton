"""
    Module for Unit Testing service.models.py file
"""


import unittest
from service.models import Model

class TestModels(unittest.TestCase):
    """ Models Test """


    def setUp(self):
        """ Runs before each test """
        Model.init_db('test')

    def tearDown(self):
        """ Runs after each test """
        pass

    def setUpClass(self):
        """ Runs before any test in class runs """
        pass

    def tearDownClass(self):
        """ Runs after all test in class runs """
        pass
