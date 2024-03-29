from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False,
            passthrough_errors=True, host='127.0.0.1', port=5000)
