# 一世无尘
# 倾尽温柔
from flask import Blueprint, render_template, request
from apps import app, salary_reload, db, Article

add_bp = Blueprint("add", __name__, url_prefix="/")


@add_bp.route('/add')
def hello_add():
    return render_template("add.html")


@add_bp.route('/add2', methods=['POST'])
def hello_add2():
    name = request.form.get('name').replace(' ', '')  # 加上.strip()去掉头和尾的空格,防止手误,加上.replace(' ', '')去掉所有空格
    dapartment = request.form.get('dapartment').replace(' ', '')
    posttion = request.form.get('posttion').replace(' ', '')
    salary = request.form.get('salary').replace(' ', '')
    article_add = Article(name=name, dapartment=dapartment, posttion=posttion, salary=salary)
    db.session.add(article_add)
    db.session.commit()
    print("数据操作成功")
    # 返回保存之后的页面
    return render_template("admin.html", salary_list=salary_reload())


@add_bp.route('/reload')
def hello_reload():
    return render_template("admin.html", salary_list=salary_reload())
