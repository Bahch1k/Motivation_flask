from flask import Flask
from flask_restful import Api
from middleware import CheckKeyMiddleware


app = Flask(__name__)
api = Api(app)
app.wsgi_app = CheckKeyMiddleware(app.wsgi_app)


import funcs

api.add_resource(funcs.List, '/motivations/')
api.add_resource(funcs.ListDetail, '/motivations/<int:id>')
api.add_resource(funcs.ListRandom, '/motivations/random/')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
