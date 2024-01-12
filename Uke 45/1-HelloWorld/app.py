from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/hei')
def hello_hei():
    return "Hei!"


if __name__ == '__main__':
    app.run(debug=True)
