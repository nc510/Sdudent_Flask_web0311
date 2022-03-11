# 一世无尘
# 倾尽温柔
from apps import Article, app
from apps.change import change_bp
from apps.add import add_bp

#注册蓝图
app.register_blueprint(add_bp)
app.register_blueprint(change_bp)

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

if __name__ == '__main__':
    app.run()

