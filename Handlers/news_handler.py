__author__ = 'Mohammad ali'


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


class NewsEditHandler(tornado.web.RequestHandler):
     def get(self, *args):
       news_id=args[0]
       newsInfo = News.select().where(News.id == news_id).get()
       self.render("news-edit.html",news=newsInfo)


     def post(self, *args):
        news_id=args[0]
        newsInfo = News.select().where(News.id == news_id).get()


        newsInfo.title = self.get_argument("news-title")
        newsInfo.body = self.get_argument("news-body")
        # date=datetime.date(datetime.now())
        kh=khayyam3.JalaliDate.today()
        # print(kh)
        kh=str(kh)
        list1=[]
        for k in kh.split("-"):
            list1.append(k)
        kh='%s/%s/%s'%(list1[0],list1[1],list1[2])

        newsInfo.date=str(kh)

        file1 = self.request.files['news-img'][0]
        original_fname = file1['filename']
        original_fname=str(original_fname)
        name=''
        for i in original_fname:
           if i==" ":
               name+="-"
           else:
               name+=i
        output_file = open("static/img/" + name, 'wb')
        output_file.write(file1['body'])


        newsInfo.img = name
        auth=Login.select().get().log
        newsInfo.author=auth
        newsInfo.save()


        self.redirect("/news")



class NewsDeleteHandler(tornado.web.RequestHandler):
     def get(self, *args):
       news_id=args[0]
       try:
           src='static/img/'+News.select().where(News.id==news_id).get().img
           os.remove(src)
       except:
           pass

       newsInfo = News.select().where(News.id == news_id).get().delete_instance()
       self.redirect("/news")



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

