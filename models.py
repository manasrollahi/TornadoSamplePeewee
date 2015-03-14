import peewee

myDB = peewee.MySQLDatabase("newspaper", host="localhost", port=3306, user="root", passwd="")

class MySQLModel(peewee.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB

class Category(MySQLModel) :
    id = peewee.PrimaryKeyField()
    name  = peewee.CharField()


class Author (MySQLModel) :
    id = peewee.PrimaryKeyField()
    fn  = peewee.CharField()
    ln = peewee.CharField()


class News(MySQLModel):
    id = peewee.PrimaryKeyField()
    title = peewee.CharField()
    body = peewee.CharField()
    date = peewee.CharField()
    category = peewee.ForeignKeyField(Category, related_name='news')
    author = peewee.ForeignKeyField(Author, related_name='news')





myDB.connect()




if __name__ == "__main__":
    # myDB.connect()
    myDB.create_tables([News,Category,Author])