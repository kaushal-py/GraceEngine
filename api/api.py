import sys
import time

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

drivers = []

class UpdateState(Resource):
    def get(self):
        start = time.time()
        args = request.args
        d=drivers[int(request.args['sessionid'])-1]
        d.update_state(args['nls'])
        end = time.time()
        program_dict = d.get_program()
        program_dict['time'] = round(end-start,5)
        return program_dict

class GetCards(Resource):
    def get(self):
        d=drivers[int(request.args['sessionid'])-1]
        return d.get_program()

class GetCode(Resource):
    def get(self):
        d=drivers[int(request.args['sessionid'])-1]
        return d.get_code()

class GetUpdates(Resource):
    def get(self):
        d=drivers[int(request.args['sessionid'])-1]
        if d.updated:
            d.updated = False
            return {"updated": True}
        else:
            return {"updated": False}

class GetVariables(Resource):
    def get(self):
        d=drivers[int(request.args['sessionid'])-1]
        return {"variables": d.store.variable_list}

class GetOutput(Resource):
    def get(self):
        d=drivers[int(request.args['sessionid'])-1]        
        return d.store.generate_output()

class GetSuggestions(Resource):
    def get(self):
        d=drivers[int(request.args['sessionid'])-1]
        args = request.args
        return d.get_suggestions(args['nlstatement'])

class ClearProgram(Resource):
    def get(self):
        d=drivers[int(request.args['sessionid'])-1]
        d.initialise_program_store()
        return {"Cleared": True}

class GetSessionId(Resource):
    def get(self):
        d = Driver()
        drivers.append(d)
        print("Driver length", len(drivers))
        return {"sessionid": len(drivers)}

api.add_resource(UpdateState, '/put')
api.add_resource(GetCards, '/get')
api.add_resource(GetCode, '/code')
api.add_resource(GetVariables, '/variables')
api.add_resource(GetOutput, '/output')
api.add_resource(GetUpdates, '/updates')
api.add_resource(GetSuggestions, '/suggest')
api.add_resource(ClearProgram, '/clear')
api.add_resource(GetSessionId, '/getsessionid')

if __name__ == '__main__':
    app.run(debug=True)