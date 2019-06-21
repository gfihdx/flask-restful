from flask_restful import reqparse, request, Resource, Api, fields, marshal_with
from models import Student, db
from operator import or_, and_
from src.common.code import make_result
from src.common.code import Code
from werkzeug.datastructures import FileStorage
from flask import jsonify
import time


class GetUserInfo(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str)
        self.reqparse.add_argument('num', type=int, required=True, help='num缺失！')
        self.reqparse.add_argument('page', type=int, required=True, help='page缺失！')
        self.args = self.reqparse.parse_args()

    # name参数可传可不传，传则根据名字搜索再分页，不传则搜索所有的数据再分页，默认过滤标记为已经删除的数据。（0：未删除，1：已删除）
    def get(self):
        name = self.args.get('name', None)
        num = self.args.get('num', None)
        page = self.args.get('page', None)
        if name:
            try:
                stu = Student.query.filter(and_(Student.name == name, Student.is_del == 0)).paginate(page=page,
                                                                                                     per_page=num)
                if stu:
                    result = []
                    for s in stu.items:
                        result.append(s.to_json())
                    return make_result(data=result)
                else:
                    return make_result(code=Code.FAIL)
            except:
                return make_result(code=Code.DATA_FAIL)
        else:
            try:
                students = Student.query.filter(Student.is_del == 0).order_by(Student.id).paginate(page=page,
                                                                                                   per_page=num)
                if students:
                    student = []
                    for s1 in students.items:
                        student.append(s1.to_json())
                    return make_result(data=student)
                else:
                    return make_result(code=Code.NOT_DATA)
            except:
                return make_result(code=Code.DATA_FAIL)


class AddStudent(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, help='name缺失！')
        self.reqparse.add_argument('sex', type=int, required=True, help='sex缺失！')
        self.reqparse.add_argument('age', type=int, required=True, help='age缺失！')
        self.reqparse.add_argument('grade', type=int, required=True, help='grade缺失！')
        self.reqparse.add_argument('source', type=int, required=True, help='source缺失！')
        self.reqparse.add_argument('face', type=str, required=True, help='face缺失！')
        self.args = self.reqparse.parse_args()

    def post(self):
        name = self.args.get('name', None)
        sex = self.args.get('sex', None)
        age = self.args.get('age', None)
        grade = self.args.get('grade', None)
        source = self.args.get('source', None)
        face = self.args.get('face', None)
        # 根据提交的数据添加用户，默认标记是否删除位为0。（0：未删除，1：已删除）
        stu = Student(name=name, sex=sex, age=age, grade=grade, source=source, face=face)
        if name and sex and age and grade and source and face:
            try:
                db.session.add(stu)
                db.session.commit()
                return make_result()
            except:
                return make_result(code=Code.DATA_FAIL)
        else:
            return make_result(code=Code.PARAM_FAIL)


class Upload(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('file', type=FileStorage, location='files')
        self.args = self.reqparse.parse_args()

    def post(self):
        # 上传文件，并保存到file文件夹下。返回重命名的文件名，以供添加接口face参数调用。
        file = self.args.get('file', None)
        file_name = f'{int(round(time.time()*1000))}.png'
        if file:
            file.save(f'./file/{file_name}')
            return make_result(data={'face': file_name})
        else:
            return make_result(code=Code.FILE_NULL)


class DelStudent(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, help='name缺失！')
        self.args = self.reqparse.parse_args()

    def delete(self):
        name = self.args.get('name', None)
        # 根据名字查询出标志为0的数据，然后再把标志更改为1.（0：未删除，1：已删除）
        if name:
            stu = Student.query.filter(and_(Student.name == name, Student.is_del == 0)).first()
            if stu:
                stu.is_del = 1
                try:
                    db.session.commit()
                    return make_result()
                except:
                    return make_result(code=Code.DATA_FAIL)
            else:
                return make_result(code=Code.NOT_DATA)
        else:
            return make_result(code=Code.PARAM_FAIL)


class UpdateStudent(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, required=True, help='id缺失！')
        self.reqparse.add_argument('name', type=str)
        self.reqparse.add_argument('sex', type=int)
        self.reqparse.add_argument('age', type=int)
        self.reqparse.add_argument('grade', type=int)
        self.reqparse.add_argument('source', type=int)
        self.reqparse.add_argument('face', type=str)
        self.args = self.reqparse.parse_args()

    def post(self):
        id = self.args.get('id', None)
        name = self.args.get('name', None)
        sex = self.args.get('sex', None)
        age = self.args.get('age', None)
        grade = self.args.get('grade', None)
        source = self.args.get('source', None)
        face = self.args.get('face', None)
        # 根据提交的ID查询出数据，然后再根据提交的数据修改相应的字段，最后提交给数据库。
        stu = Student.query.filter(Student.id == id).first()
        if stu:
            if name or sex or age or grade or source or face:
                if name:
                    stu.name = name
                if sex:
                    stu.sex = sex
                if age:
                    stu.age = age
                if grade:
                    stu.grade = grade
                if source:
                    stu.source = source
                if face:
                    stu.face = face
                db.session.add(stu)
                try:
                    db.session.commit()
                    return make_result()
                except:
                    return make_result(code=Code.DATA_FAIL)
            else:
                return make_result(code=Code.FAIL)
        else:
            return make_result(code=Code.NOT_DATA)
