# 一世无尘
# 倾尽温柔
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

#创建APP
app = Flask(__name__,template_folder='../templates',static_folder="../static",static_url_path="/static")

# flash需要加密内容
app.secret_key = "test"
#app.secret_key = str(os.urandom(24))

from apps import config
# HOSTNAME = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'zl_flask'
# USERNAME = 'root'
# PASSWORD = 'root'
# DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

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

def salary_reload():
    salary_list_reload = Article.query.all()
    return salary_list_reload

@app.route('/login', methods=["POST"])
def hello_login():
    # 登陆到服务器
    # 获取了用户与密码以后,校验
    '''
    for sal in salary_list:
        if sal['name'] == username:
            print("用户存在")
        else:
            print("用户不存在")
    '''

    # request:请求对象，请求方式，数据
    # 1.判断请求方式
    if request.method == "POST":
        # 加上.strip()去掉头和尾的空格,防止手误,加上.replace(' ', '')去掉所有空格
        username = request.form.get('username').replace(' ', '')
        password = request.form.get('password').replace(' ', '')
        print(username, password)
        #if not all([username,password]):
            #flash(u"不参数完整")
        if username != "admin" or password != "admin":
            flash(u"用户名或密码错误")
            return render_template("index.html")
        else:
            #flash(u"允许登陆")
            return render_template("admin.html", salary_list=salary_reload())

@app.route('/')
def hello_world():
    # 创建数据库引擎
    engine = db.get_engine()
    #salary_reload()
    #conn = engine.connect()
    #conn.close()
    with engine.connect() as conn:
        result = conn.execute("select 1")
        print(result.fetchone())
        print(engine)
        print("打开了首页")
    return render_template("index.html")