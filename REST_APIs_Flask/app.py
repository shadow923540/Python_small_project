from flask import Flask


app = Flask(__name__)

#What request do we want?

@app.route('/') # 'http://www.google.com/'
def home():
    return "Hello, world!"


app.run(port=5000)