import json
from flask import Flask
from flask_restful import Resource, Api

from ..engine.engine_driver import Driver

app = Flask(__name__)
api = Api(app)

d = Driver()

class HelloWorld(Resource):
    def get(self, natural_sentence):
        c = d.drive(natural_sentence)
        return c.generate_card()

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)