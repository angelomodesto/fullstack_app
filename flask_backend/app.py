from flask import Flask, request
from math_util import addTimesTwo

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/feed')
def get_feed():
    return "Fetching videos for you to watch... Please wait."

@app.route('/addTimesTwo')
def search():
    num1Str = request.args.get('num1')
    num2Str = request.args.get('num2')

    num1 = int(num1Str)
    num2 = int(num2Str)

    result = addTimesTwo(num1, num2)
    resultStr = str(result)

    return resultStr

if __name__ == '__main__':
    app.run(debug=True)
