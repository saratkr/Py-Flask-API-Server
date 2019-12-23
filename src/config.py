#from flask_marshmallow import Marshmallow
import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = '12345abcdabcd'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_USER = 'admin'
    ADMIN_PASS = 'admin'
