from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql
app = Flask(__name__)  # 实例化一个Flask

#连接数据库配置: SQLALCHEMY_DATABASE_URI。
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/zl_flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "1e3df42bbfe146c785f422611d6e7429"
app.debug = True


# 创建数据库引擎
engine = db.get_engine()
inspector = inspect(engine)
#salary_reload()
#conn = engine.connect()
#conn.close()
with engine.connect() as conn:
    result = conn.execute("select 1")
    print(result.fetchone())
    print(engine)
    print("打开了首页")

    db.reflect(app=app)     #1、映射app数据库中的表（app其实就是本程序的flask实例，已连接到数据库）
    tables=db.metadata.tables   #2、取得所有数据库（返回：immutabledict，里面实际包含了数据库中所有表的结构
    print(tables)