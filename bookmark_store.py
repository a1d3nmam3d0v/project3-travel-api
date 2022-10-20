from peewee import *

db = SqliteDatabase('bookmarks.sqlite')

class BookmarkType(Model):
    id = IntegerField()
    name = CharField()

    class Meta:
        database = db

class Bookmark(Model):
    name = CharField()
    url = CharField()
    type_id = ForeignKeyField(BookmarkType, backref='bookmarks')
    
    class Meta:
        database = db

db.connect()
db.create_tables([BookmarkType, Bookmark])

def get_bookmarks():
    bookmark_list = []
    for bookmark in Bookmark.select():
        bookmark_list.append(bookmark)
    return bookmark_list
