import sys

import json
from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_cors import CORS

# Local libraries
sys.path.insert(0, '../')
from engine.engine_driver import Driver

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

d = Driver()

class HelloWorld(Resource):
    def get(self):
        args = request.args
        print(args)
        c = d.drive(args['nls'])
        program = {"program" : [c.generate_card()]}
        return program

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)