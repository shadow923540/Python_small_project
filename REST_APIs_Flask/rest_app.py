from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api= Api(app)

items []


class Item(Resource):
    def get(self, name):
        return {'student': name}

api.add_resource(Item, '/item/<string:name>')


app.run(port=5000)