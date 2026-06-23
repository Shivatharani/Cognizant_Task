from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


# Forward Course Requests

@app.route("/api/courses/<path:path>", methods=["GET"])
def proxy_courses(path):

    url = f"http://127.0.0.1:5001/api/courses/{path}"

    response = requests.get(url)

    return (

        response.json(),

        response.status_code

    )


# Forward Student Requests

@app.route(

    "/api/students/<path:path>",

    methods=["GET", "POST"]

)

def proxy_students(path):


    url = f"http://127.0.0.1:5002/api/students/{path}"


    if request.method == "POST":


        response = requests.post(

            url,

            json=request.get_json()

        )


    else:


        response = requests.get(url)


    return (

        response.json(),

        response.status_code

    )



@app.route("/")

def home():

    return {

        "message":

        "API Gateway Running"

    }



if __name__ == "__main__":

    app.run(

        port=5000,

        debug=True

    )