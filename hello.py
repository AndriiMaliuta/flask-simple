import json, sys

from flask import Flask, jsonify, abort, request, escape, url_for
from models import db, Cat
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cat.db"
db.init_app(app)
cats = {
    "cats": [
        {"name": "Simba", "age": 6}
    ]
}


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/cats")
def cats():
    # json.dump()
    return jsonify({})


@app.route("/<slug>")
def cats_slug(slug):
    try:
        cat = cats[slug]
    except KeyError:
        abort(404)
    return jsonify(cat)


@app.route('/name')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


if __name__ == "__main__":
    if "createdb" in sys.argv:
        with app.app_context():
            db.create_all()
        print("Database created!")

    elif "seeddb" in sys.argv:
        with app.app_context():
            p1 = Cat(slug="rover", name="Rover",
                       image_url="http://example.com/rover.jpg")
            db.session.add(p1)
            p2 = Cat(slug="spot", name="Spot",
                       image_url="http://example.com/spot.jpg")
            db.session.add(p2)
            db.session.commit()
        print("Database seeded!")

    else:
        app.run(debug=True)
