from flask import Flask, request

app = Flask(__name__)

@app.route('/push', methods=['POST'])
def index():
    print(request.json)