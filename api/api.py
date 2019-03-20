import sys

import json
from flask import Flask
from flask import request
from flask_restful import Resource, Api

# Local libraries
sys.path.insert(0, '../')
from engine.engine_driver import Driver

app = Flask(__name__)
api = Api(app)

d = Driver()

class HelloWorld(Resource):
    def get(self):
        args = request.args
        print(args)
        c = d.drive(args['nls'])
        return c.generate_card()

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)