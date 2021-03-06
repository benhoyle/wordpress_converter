import os

# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import Caching extension
from flask_cache import Cache

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object(os.environ.get('APP_SETTINGS'))

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

# define the cache config keys, remember that it can be done in a settings file
app.config['CACHE_TYPE'] = 'simple'
# Change this to memcache in production

# register the cache instance and binds it on to your app 
app.cache = Cache(app)