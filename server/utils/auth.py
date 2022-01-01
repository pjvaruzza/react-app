import functools
from flask import request, make_response

SESSION_TOKEN = "A-RANDOMLY-GENERATED-SESSION-TOKEN"

# decorator for protecting routes--wraps the route, almost intercepting it
def auth_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if request.method == 'GET':
            # get the session cookie from the request header
            # read about request headers here - https://developer.mozilla.org/en-US/docs/Glossary/Request_header
            session = request.cookies.get("sessionToken")
        else:
            session = "Maybe another permission for other request types?"

        if session == SESSION_TOKEN:
            # Do some stuff here if you want
            return view(**kwargs)
        else:
            status_code = 403 # forbidden status code, access denied
            data = {"message": "Sorry, you don't have permission to see my secret. Go to '/main' first."}
            response = make_response(data, status_code)
            return response
    return wrapped_view
