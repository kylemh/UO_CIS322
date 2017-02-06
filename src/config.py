import json
import os
import pathlib

'''
NOTE:
1) the APP_SECRET_KEY is secret. it should be generated in a way that makes everyone comfortable.
possible suggestions: A.) import os; os.urandom(size_bytes) B.) import uuid; str(uuid.uuid4())

2) DB_LOCATION is a string that can be passed to psycopg2 to connect to the db
'''

cpath = pathlib.Path(os.path.realpath(__file__)).parent.joinpath('config.base.json')

with cpath.open() as conf:
	c = json.load(conf)
	DB_NAME = c['database']['dbname']
	HOST = c['database']['dbhost']
	PORT = c['database']['dbport']

APP_SECRET_KEY = ""  # TODO: string, see note 1 above
DB_LOCATION = ("dbname=" + DB_NAME, "host=" + HOST, "port=" + PORT)  # TODO: string, see note 2 above
DEBUG = True
