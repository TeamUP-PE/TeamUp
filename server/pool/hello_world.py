from flask import request, Blueprint, Response

hello = Blueprint('hello', __name__)


@hello.route('/')
def hello_world():
  return Response(
    'Hello World!!!',
    status=200
  )


@hello.route('mopa/', methods=['POST'])
def hello_world_post():
  return Response(
    'Hello World!!!',
    status=200
  )
