__author__ = 'Mohammad'


import tornado
from  models import *
import peewee
import os
from datetime import datetime
from pycket.session import SessionManager
import khayyam3


class NewsHandler(tornado.web.RequestHandler):
     def get(self):
             news = News.select().order_by(News.id.desc())
             self.render('news.html', news = news)


     def post(self,*args):
         self.render("news-new.html")


class NewsNewHandler(tornado.web.RequestHandler):
     def get(self, *args):
         cat=Category.select()
         aut=Author.select()
         self.render("news-new.html",cat=cat,aut=aut)


     def post(self, *args):

       newsTitle = self.get_argument("news-title")
       newsBody=self.get_argument("news-body")
       # date=datetime.date(datetime.now())
       # datetime.astimezone()
       # print(date)
       kh=khayyam3.JalaliDate.today()
       kh=str(kh)
       list1=[]
       for k in kh.split("-"):
            list1.append(k)
       kh='%s/%s/%s'%(list1[0],list1[1],list1[2])
       newsDate=str(kh)
       newsAuthor=self.get_argument("news-aut")
       newscat=self.get_argument("news-cat")


       newsInfo = News.create(
           title=newsTitle,
           body=newsBody,
           date=newsDate,
           category=newscat,
           author=newsAuthor
       )

       self.redirect("/news")

