"""
    This module holds the model for our application
"""

from cloudant.client import Cloudant

class Model(object):
    client = None
    database = None

    def init_db(dbname):
        creds = {
            'username': 'admin',
            'password': 'pass',
            'url': 'http://admin:pass@127.0.0.1:5984/'
            }

        try:
            Model.client = Cloudant(creds['username'],
                                  creds['password'],
                                  url=creds['url'],
                                  connect=True,
                                  auto_renew=True
                                 )
        except ConnectionError:
            raise AssertionError('Cloudant service could not be reached')

        try:
            Model.database = Model.client[dbname]
        except KeyError:
            # Create a database using an initialized client
            Model.database = Model.client.create_database(dbname)


        # check for success
        if not Model.database.exists():
            raise AssertionError('Database [{}] could not be obtained'.format(dbname))
