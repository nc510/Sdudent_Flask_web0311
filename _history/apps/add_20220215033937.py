# 一世无尘
# 倾尽温柔
from flask import Blueprint, render_template, request
from apps import app

add_bp = Blueprint("add", __name__, url_prefix="/")


@add_bp.route('/add3')
def hello_add():
    return render_template("add.html")


@add_bp.route('/add2', methods=['POST'])
def hello_add2():
    name = request.form.get('name').replace(' ', '')  # 加上.strip()去掉头和尾的空格,防止手误,加上.replace(' ', '')去掉所有空格
    dapartment = request.form.get('dapartment').replace(' ', '')
    posttion = request.form.get('posttion').replace(' ', '')
    salary = request.form.get('salary').replace(' ', '')
    article = app.Article(name=name, dapartment=dapartment, posttion=posttion, salary=salary)
    app.db.session.add(article)
    app.db.session.commit()
    print("数据操作成功")
    # 返回保存之后的页面
    return render_template("admin.html", salary_list=app.salary_reload())


@add_bp.route('/add')
def hello_reload():
    return "刷新页面"#render_template("admin.html", salary_list=app.salary_reload())
