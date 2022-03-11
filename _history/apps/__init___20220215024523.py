# 一世无尘
# 倾尽温柔
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apps.add import bp as add_bp

import apps.config

#创建APP
app_0 = Flask(__name__,template_folder='../templates',static_folder="../static",static_url_path="/static")

# flash需要加密内容
app_0.secret_key = "test"
#app.secret_key = str(os.urandom(24))


#连接数据库,地址在apps.Sql_connect.DB_URI
app_0.config['SQLALCHEMY_DATABASE_URI'] = apps.config.DB_URI
app_0.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 跟踪警告修改,True不提示
app_0.config['PERMANENT_SESSION_LIFETIME'] = 60  #设置生命周期1分钟

db = SQLAlchemy(app_0) #创建数据库对象

class Article(db.Model):
    __tablename__ = 'data_myhome'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    dapartment = db.Column(db.String(200), nullable=False)
    posttion = db.Column(db.String(200), nullable=False)
    salary = db.Column(db.Integer, nullable=False)

db.create_all()


from apps.change import bp as change_bp

#注册蓝图
app_0.register_blueprint(add_bp)
app_0.register_blueprint(change_bp)