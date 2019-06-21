class FlaskSetting:
    DEBUG = True
    SECRET_KEY = "DragonFire"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./db/i-demo.db'  # app的配置，指定数据库路径
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:GFIHDX1988yxl.@localhost:3306/interface'
    # 这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名interface
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True  # 执行时，可以看到sql语句
