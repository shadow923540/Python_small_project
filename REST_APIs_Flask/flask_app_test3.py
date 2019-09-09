from flask import Flask, jsonify

app = Flask(__name__)

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

@app.route('/fib/<int:fib>')
def get_store(fib):
    if fib <= 1:
        return jsonify({'Fib': fib})
    else:
        return jsonify({'Fib': (recur_fibo(fib - 1) + recur_fibo(fib - 2))})


app.run(port=5000)