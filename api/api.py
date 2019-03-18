import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        with open('demos/demo.json', 'r') as fp:
            data = json.load(fp)
        # print(data)
        return data

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)