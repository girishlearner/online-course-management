import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x0c)i\xf1\nv\xb5Y\x04\xe7D\xef\x7f\xd9K\xcf'

    MONGODB_SETTINGS = { 'db' : 'UTA_Encrollment'}