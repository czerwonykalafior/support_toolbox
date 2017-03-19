import os

# General Flask app settings
DEBUG = os.environ.get('DEBUG', None)
SECRET_KEY = os.environ.get('SECRET_KEY', None)

SQLALCHEMY_DATABASE_URI = 'postgres://stiven:zajzajer@127.0.0.1:5432/stiven'
SQLALCHEMY_TRACK_MODIFICATIONS = False