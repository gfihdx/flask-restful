# flask-restful
运用flask、flask-restful开发rest风格的接口，并使用蓝图增加代码的延展性和可扩展性。


db:由于运用的是sqlite数据库，此处为存放数据库文件。
file:模拟的上传文件的操作，凡是通过上传文件接口上传的文件都存在此处。
src:
  --common : 写一个公共的方法
  --module: 存放相关蓝图
    --user : user为本项目的一个蓝图。（如有需要可扩展其它蓝图文件，只需要在主app中注册该蓝图及可）
venv : 本项目的虚拟目录
app  :主启动文件
models : 数据库orm
settings  ： 本项目相关设置


本项目实现的接口为：

1、查询：/get/user/info
  参数:name   名字，可为空，为空及查询全部
  参数：page  页码   必传
  参数：num   每页条数  必传
  
  
2、添加：/add/stu
  参数：name     名字
  参数：sex      性别：1男 2女
  参数：age      年龄
  参数：grade    年级  1一年级 2二年级以此类推
  参数：source   分数
  参数：face     头像  此数据为上传接口返回
  
 3、上传头像：/upload/
  参数：file   文件
  
  4、删除：/del/stu/
    参数：name   名字 必传
    
    
  5、修改：/update/stu/
    参数：id   学生id，可在查询接口获取，必传
    以下参数，有修改则传，无修改则不传。
    参数：name     名字
    参数：sex      性别：1男 2女
    参数：age      年龄
    参数：grade    年级  1一年级 2二年级以此类推
    参数：source   分数
    参数：face     头像  此数据为上传接口返回
