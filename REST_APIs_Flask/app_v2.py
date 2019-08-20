from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
            'name': 'My Item',
            'price': 15.99
            }
        ]
    }
]

#POST /store data: {name:}
@app.route('/store', methods=['POST']) #app.route is GET by default
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>') #'http://127.0.0.1:5000/store/some_name'
#Special Flask sytax (the same "name") should be in get_store
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

#POST /store/<string:name>/item {name, price:}
@app.route('/stpre/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


app.run(port=5000)