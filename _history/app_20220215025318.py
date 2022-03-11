# 一世无尘
# 倾尽温柔
from flask import render_template, request, flash
from apps import Article, app, db


def salary_reload():
    salary_list_reload = Article.query.all()
    return salary_list_reload

'''数据库增删改查
@app_0.route('/article')
def article_view():
        pass
        # 1,添加数据
        article = Article(name="钢铁人2", dapartment="自己人2",posttion="自己人2",salary=30002)
        db.session.add(article)
        # 提交一下
        db.session.commit()
        return "数据操作成功"

        # 2,查询数据
        #filter_by返回一个类列表的对象,所以要中括号取出来
        #article = Article.query.filter_by(id=1)[0]
        #print(article.name)
        #return "数据查询成功"

        # 3,修改数据
        # article_g = Article.query.filter_by(id=1)[0]
        # article_g.content = "yyy"
        # db.session.commit()
        # return "数据操作成功"

        # 4,删除数据
        # Article.query.filter_by(id=1).delete()
        # db.session.commit()
        # return "数据删除成功"
'''

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
    salary_reload()
    #conn = engine.connect()
    #conn.close()
    with engine.connect() as conn:
        result = conn.execute("select 1")
        print(result.fetchone())
        print(engine)
        print("打开了首页")
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
