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

class UpdateState(Resource):
    def get(self):
        args = request.args
        d.update_state(args['nls'])
        return d.get_program()

class GetCards(Resource):
    def get(self):
        return d.get_program()

class GetCode(Resource):
    def get(self):
        return d.get_code()

class GetUpdates(Resource):
    def get(self):
        if d.updated:
            d.updated = False
            return {"updated": True}
        else:
            return {"updated": False}

class GetVariables(Resource):
    def get(self):
        return {"variables": d.store.variable_list}

class GetOutput(Resource):
    def get(self):
        return d.store.generate_output()

class GetSuggestions(Resource):
    def get(self):
        args = request.args
        return d.get_suggestions(args['nlstatement'])

class ClearProgram(Resource):
    def get(self):
        d.initialise_program_store()
        return {"Cleared": True}

api.add_resource(UpdateState, '/put')
api.add_resource(GetCards, '/get')
api.add_resource(GetCode, '/code')
api.add_resource(GetVariables, '/variables')
api.add_resource(GetOutput, '/output')
api.add_resource(GetUpdates, '/updates')
api.add_resource(GetSuggestions, '/suggest')
api.add_resource(ClearProgram, '/clear')

if __name__ == '__main__':
    app.run(debug=True)