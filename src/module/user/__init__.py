from flask_restful import Api
from flask import Blueprint

student = Blueprint("user", __name__)
resource = Api(student)

from .view import *

resource.add_resource(GetUserInfo, '/get/user/info/')
resource.add_resource(AddStudent, '/add/stu/')
resource.add_resource(Upload, '/upload/')
resource.add_resource(DelStudent, '/del/stu/')
resource.add_resource(UpdateStudent, '/update/stu/')
