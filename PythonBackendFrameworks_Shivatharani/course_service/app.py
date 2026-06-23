from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///course.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Course(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    code = db.Column(db.String(50), unique=True)


@app.route("/")
def home():

    return {

        "message": "Course Service Running"

    }


@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):

    course = Course.query.get(id)

    if course is None:

        return jsonify({

            "error": "Course not found"

        }), 404


    return jsonify({

        "id": course.id,

        "name": course.name,

        "code": course.code

    })


if __name__ == "__main__":

    with app.app_context():

        db.create_all()


        if Course.query.count() == 0:

            c1 = Course(

                name="Python",

                code="CS101"

            )

            c2 = Course(

                name="Java",

                code="CS102"

            )

            db.session.add(c1)

            db.session.add(c2)

            db.session.commit()


    app.run(

        port=5001,

        debug=True

    )