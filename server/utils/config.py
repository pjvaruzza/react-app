import os

# imports variables from the environment and wraps them into a Config class
class Config:

    SECRET_KEY = os.environ['SECRET_KEY'] # this should be a secret !

    CORS_SUPPORTS_CREDENTIALS = True # must be true to permit cookies in request header
    CORS_ALLOW_ORIGIN = os.environ['CORS_ALLOW_ORIGIN'] # Who can make requests
