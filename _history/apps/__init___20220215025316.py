# 一世无尘
# 倾尽温柔
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#创建APP
app = Flask(__name__,template_folder='../templates',static_folder="../static",static_url_path="/static")

# flash需要加密内容
app.secret_key = "test"
#app.secret_key = str(os.urandom(24))

import config
#连接数据库,地址在apps.Sql_connect.DB_URI
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 跟踪警告修改,True不提示
app.config['PERMANENT_SESSION_LIFETIME'] = 60  #设置生命周期1分钟

db = SQLAlchemy(app) #创建数据库对象

class Article(db.Model):
    __tablename__ = 'data_myhome'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    dapartment = db.Column(db.String(200), nullable=False)
    posttion = db.Column(db.String(200), nullable=False)
    salary = db.Column(db.Integer, nullable=False)

db.create_all()
from change import change_bp
from add import add_bp


#注册蓝图
app.register_blueprint(add_bp)
app.register_blueprint(change_bp)