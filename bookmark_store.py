from peewee import *

db = SqliteDatabase('bookmarks.sqlite')

class BookmarkType(Model):
    id = IntegerField(primary_key = True)
    name = CharField()

    class Meta:
        database = db

class Bookmark(Model):
    type_id = ForeignKeyField(BookmarkType, backref='bookmarks')
    name = CharField()
    country = CharField()
    city = CharField()
    url = CharField()
    
    class Meta:
        database = db

db.connect()
# db.create_tables([BookmarkType, Bookmark])
# type1 = BookmarkType(name='video')
# type1.save()
# type2 = BookmarkType(name='restaurant')
# type2.save()

def get_bookmarks():
    bookmark_list = []
    for bookmark in Bookmark.select():
        bookmark_list.append(bookmark)
    return bookmark_list

def add_bookmark(type_id, name, country, city, url):
    new_bookmark = Bookmark(type_id=type_id, name=name, country=country, city=city, url=url)
    new_bookmark.save()