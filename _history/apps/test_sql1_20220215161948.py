from flask import Blueprint, render_template, request
from apps import app, salary_reload, db, Article

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