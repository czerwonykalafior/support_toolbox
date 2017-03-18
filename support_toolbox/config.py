import os

# General Flask app settings
DEBUG = os.environ.get('DEBUG', None)
SECRET_KEY = os.environ.get('SECRET_KEY', None)

SQLALCHEMY_DATABASE_URI = 'postgres://postgres:zajzajer@127.0.0.1:5432/support_toolbox'
SQLALCHEMY_TRACK_MODIFICATIONS = False