from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api= Api(app)

items= []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item #We don't have to use jsonify because flask_restful can handle dic
        return {'item': None}, 404

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201 #Let know the app that we add an item


api.add_resource(Item, '/item/<string:name>')






app.run(port=5000, debug=True)