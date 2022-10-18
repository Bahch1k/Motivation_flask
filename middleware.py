from werkzeug.wrappers import Request, Response
import os
from dotenv import load_dotenv

load_dotenv()


class CheckKeyMiddleware():
    def __init__(self, app):
        self.app = app
        self.key = os.getenv('API_KEY')

    def __call__(self, environ, start_response):
        request = Request(environ)
        api_key = request.headers['Authorization']

        if self.key == api_key:
            return self.app(environ, start_response)

        response = Response("Permission denied", mimetype='application/json', status=403)
        return response(environ, start_response)
