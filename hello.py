from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/cats")
def cats():
    return jsonify({"cats": [ { "name": "Simba", "age": 6 } ]})


if __name__ == "__main__":
    app.run(debug=True)
