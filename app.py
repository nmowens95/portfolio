from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world, im heree"

@app.route('/user/<name>')
def user(name):
    personal = f'<h1>Hello, {name}!</h1>'


if __name__ == '__main__':
    app.run(port=4999, debug=True)