# 一世无尘
# 倾尽温柔
from flask import Blueprint, render_template, request
from apps import salary_reload, Article, db
change_bp = Blueprint("change", __name__, url_prefix="/")

@change_bp.route('/change/<name>')
def hello_change(name):
    # 逻辑 先找到信息,然后再修改
    print("运算修改")
    for salary in salary_reload():
        article = Article.query.filter_by(id=salary.id)[0]
        print(article.name)
        if article.name == name:
            # 修改,跳出修改页面
            print("运行修改查找")
            return render_template("change.html", user1=article)

@change_bp.route('/changed/<name>', methods=["POST"])
def hello_changed(name):
    # 修改 拿到提交的信息
    for salary in salary_reload():
        #在数据库中查找对应的项
        article = Article.query.filter_by(id=salary.id)[0]
        if article.name == name:
            article.name = request.form.get('name').replace(' ', '')  # 加上.strip()去掉头和尾的空格,防止手误,加上.replace(' ', '')去掉所有空格
            article.dapartment = request.form.get('dapartment').replace(' ', '')
            article.posttion = request.form.get('posttion').replace(' ', '')
            article.salary = request.form.get('salary').replace(' ', '')
            db.session.commit()
            print("数据修改成功")
            # 修改,跳出修改页面
            break
    return render_template("admin.html", salary_list=salary_reload())

# 删除数据
@change_bp.route('/delete/<name>')
def hello_delete(name):
    # 删除逻辑 先找到信息,然后再删除
    for salary in salary_reload():
        article = Article.query.filter_by(id=salary.id)[0]
        if article.name == name:
            # 列表删除元素的几种方式
            Article.query.filter_by(id=salary.id).delete()
            db.session.commit()
    return render_template("admin.html", salary_list=salary_reload())
