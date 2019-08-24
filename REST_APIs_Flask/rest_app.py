from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api= Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items= []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item #We don't have to use jsonify because flask_restful can handle dic
        item = next(filter(lambda x: x['name'] == name,items), None) # Next give us first item in filter function
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name,items), None) is not None:
            return {'message': 'An item exist'}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 #Let know the app that we add an item

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')






app.run(port=5000, debug=True)