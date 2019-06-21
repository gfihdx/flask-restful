from flask import Flask, abort
from flask_restful import reqparse, Api, Resource
from flask_sqlalchemy import SQLAlchemy
from operator import or_, and_
import settings
import flask_restful
from src.common.code import make_result
from src.common.code import Code

app = Flask(__name__, static_url_path='')
app.config.from_object("settings.FlaskSetting")  # 导入app的配置信息。

db = SQLAlchemy(app)  # 实例化db。

from models import Student  # 需要把创建的数据库类导入，不然创建表会失败。

from src.module.user import student

app.register_blueprint(student)  # 注册蓝图

#
# def my_abort(http_status_code, *args, **kwargs):
#     if http_status_code == 400:
#         # 重定义400返回参数
#         abort(make_result(code=Code.PARAM_FAIL))
#
#     return abort(http_status_code)
#
#
# # 把flask_restful中的abort方法改为我们自己定义的方法
# flask_restful.abort = my_abort


if __name__ == '__main__':
    app.run()
