from flask import request, Blueprint, Response, abort

from pool.models import User

hello = Blueprint('hello', __name__)


@hello.route('/')
def hello_world():
    return Response(
        'Hello World!!!',
        status=200
    )


@hello.route('/mopa/', methods=['POST'])
def hello_world_post():
    return Response(
        'Hello World!!!',
        status=200
    )


@hello.route('/create/', methods=['POST'])
def create_user():
    try:
        if not request.json():
            return abort(500)
        User(
            name=request.json.get('name'),
            email=request.json.get('email'),
            password=request.json.get('password')
        ).create()
        return Response(
            'User successfully created!',
            200
        )
    except Exception as e:
        return Response(
            'Bad Request: {}'.format(e),
            status=401
        )