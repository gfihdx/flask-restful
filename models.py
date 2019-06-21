from app import db
from flask import jsonify
from marshmallow import Schema, fields
import datetime


# ORM创建数据库存表

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), )
    sex = db.Column(db.Integer, )
    age = db.Column(db.Integer, )
    grade = db.Column(db.Integer)
    source = db.Column(db.Integer)
    face = db.Column(db.String(500))
    is_del = db.Column(db.Integer)

    def __init__(self, name, sex, age, grade, source, face, is_del=0):
        self.name = name
        self.sex = sex
        self.age = age
        self.grade = grade
        self.source = source
        self.face = face
        self.is_del = is_del

    def __repr__(self):
        return f'{self.name} is face {self.face}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'sex': self.sex,
            'age': self.age,
            'grade': self.grade,
            'source': self.source,
            'face': self.face,
            'is_del': self.is_del
        }


class StudentSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    sex = fields.Integer()
    age = fields.Integer()
    grade = fields.Integer()
    source = fields.Integer()
    rank = fields.Integer()
