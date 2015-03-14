__author__ = 'Mohammad ali'

import tornado
from  models import *
import peewee

class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('Search-news.html')

    def post(self, *args):
        srch=self.get_argument("srch")
        # print(srch)
        news = News.select()
        ST_news=[]
        for n in news:
            for t in n.title.split():
                for s in srch.split():
                    if t==s:
                        if News.select().where(News.title==n.title).get() not  in ST_news:
                            ST_news.append(News.select().where(News.title==n.title).get())
        for n in news:
            for t in n.body.split():
                for s in srch.split():
                    if t==s:
                        if News.select().where(News.body==n.body).get() not  in ST_news:
                            ST_news.append(News.select().where(News.body==n.body).get())
        self.render("Show-Search.html", news=ST_news)

class SearchShowHandler(tornado.web.RequestHandler):
    def get(self,*args):
        pass
#         # news=News.select().where(News.title==args).get()
#         news = News.select()
#         ST_news=[]
#         for title in news.title:
#             for t in title.split():
#                 for s in args.split():
#                     if t==s:
#                         if News.select().where(News.title==title).get() not  in ST_news:
#                             ST_news.append(News.select().where(News.title==title).get())())
#         self.render("Show-Search.html", news=ST_news)
#
    def post(self,*args):
        pass
#         # news=News.select().where(News.title==args)
#         # # srch=self.get_argumen("srch")
#         #
#         #
#         # self.redirect("/showsearch")