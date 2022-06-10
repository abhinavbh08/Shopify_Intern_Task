import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "inventory-tracker"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
