from flask import Flask, request

app = Flask(__name__)

@app.route('/push', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'hello'
    else:
        print(request.json)
        return request.json

@app.route('/hydropro', methods=['GET', 'POST'])
def hydropro():
    if request.method == 'GET':
        return 'hello'
    else:
        print(request.json)
        return request.json

if __name__ == "__main__":
    app.run()