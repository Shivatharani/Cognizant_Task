from flask import Blueprint

from flask import jsonify

from flask import request


from extensions import db

from .models import Course

from .models import Student

from .models import Enrollment


courses_bp = Blueprint(

'courses',

__name__,

url_prefix='/api/courses'

)



def make_response_json(data,status):

    return jsonify({

        "status":"success",

        "data":data

    }),status



@courses_bp.route('/',methods=['GET'])

def get_courses():

    courses=Course.query.all()

    result=[c.to_dict() for c in courses]

    return make_response_json(result,200)




@courses_bp.route('/',methods=['POST'])

def add_course():

    data=request.get_json()


    if(

        not data

        or

        'name' not in data

        or

        'code' not in data

        or

        'credits' not in data

    ):

        return jsonify({

        "error":"Missing required fields"

        }),400



    course=Course(

        name=data['name'],

        code=data['code'],

        credits=data['credits']

    )


    db.session.add(course)

    db.session.commit()


    return make_response_json(

        course.to_dict(),

        201

    )





@courses_bp.route('/<int:id>',methods=['GET'])

def get_course(id):


    course=Course.query.get_or_404(id)


    return make_response_json(

        course.to_dict(),

        200

    )






@courses_bp.route('/<int:id>',methods=['PUT'])

def update_course(id):


    course=Course.query.get_or_404(id)


    data=request.get_json()


    course.name=data.get(

        'name',

        course.name

    )


    course.code=data.get(

        'code',

        course.code

    )


    course.credits=data.get(

        'credits',

        course.credits

    )


    db.session.commit()


    return make_response_json(

        course.to_dict(),

        200

    )






@courses_bp.route('/<int:id>',methods=['DELETE'])

def delete_course(id):


    course=Course.query.get_or_404(id)


    db.session.delete(course)

    db.session.commit()


    return '',204




@courses_bp.route(

'/<int:id>/students/',

methods=['GET']

)

def get_students(id):


    enrollments=Enrollment.query.filter_by(

        course_id=id

    ).all()


    students=[

        e.student.to_dict()

        for e in enrollments

    ]


    return make_response_json(

        students,

        200

    )