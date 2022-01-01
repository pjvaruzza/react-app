from flask import Blueprint, request, make_response

from server.utils import auth_required, SESSION_TOKEN

# Start by creating an instance of Blueprint which will then decorate all our routes
bp = Blueprint('main', __name__)

# This route is not protected by authentication
@bp.get('/get/unprotected')
def get_data():
    status_code = 200 # 200 status code means 'success'! Read more about status codes here - https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    data = {
        "messager": "Me, of course!",
        "message": "Hello, World!",
        "session": SESSION_TOKEN # This session token will give the user access to the protected route
    } # some data that we're bundling and sending to the client in a dictionary which will convert to json
    return data, status_code

# This route IS protected by authentication
@bp.get('/get/protected')
@auth_required # this decorator is 'protecting' the route
def get_protected_data():
    status_code = 200
    data = {
        "messager": "Me, of course! But this time protected.",
        "message": "I love cheese... it's gouda!"
    }
    return data, status_code

# Receives data from the client then responds to confirm reception
@bp.post('/post')
def post_data():
    data = request.json # take the json from the request
    status_code = 200
    data = {"message": f"You shared something! '{data['secret']}'"} # create json package for response
    response = make_response(data, status_code)
    return response
