from flask import Flask


app = Flask(__name__)

#What request do we want?


#POST /store data: {name:}
@app.route('/store', methods=['Post']) #app.route is GET by default
def create_store():
    pass

#GET /store/<string:name>
@app.route('/store/<string:name>') #'http://127.0.0.1:5000/store/some_name'
#Special Flask sytax (the same "name") should be in get_store
def get_store(name):
    pass

#GET /store
@app.route('/store')
def get_stores():
    pass

#POST /store/<string:name>/item {name, price:}
@app.route('/stpre/<string:name>/item', methods=['Post'])
def create_item_in_store(name):
    pass

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


app.run(port=5000)