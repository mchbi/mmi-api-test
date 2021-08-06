from flask import Flask, request

app = Flask(__name__)

@app.route('/push', methods=['POST'])
def index():
    if request.method == 'GET':
        return 'hello'
    else:
        return request.json