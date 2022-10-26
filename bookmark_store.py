from peewee import *

db = SqliteDatabase('bookmarks.sqlite')

class BookmarkType(Model):
    id = IntegerField(primary_key=True)
    name = CharField(unique=True)

    class Meta:
        database = db

class Bookmark(Model):
    type_id = ForeignKeyField(BookmarkType, to_field='id')
    name = CharField()
    country = CharField()
    city = CharField()
    url = CharField()
    
    class Meta:
        database = db

        indexes = (
            (('type_id', 'name', 'country', 'city', 'url'), True),
        )

db.connect()
#db.create_tables([BookmarkType, Bookmark])
#type1 = BookmarkType(name='video')
#type1.save()
#type2 = BookmarkType(name='restaurant')
#type2.save()

def get_bookmarks():
    bookmark_list = []
    for bookmark in Bookmark.select():
        bookmark_list.append(bookmark)
    return bookmark_list

def add_bookmark(type_id, name, country, city, url):
    try:
        new_bookmark = Bookmark(type_id=type_id, name=name, country=country, city=city, url=url)
        new_bookmark.save()
    except Exception as ex:
        print(ex)
        return None

def add_type(name):
    try:
        new_type = BookmarkType(name=name)
        new_type.save()
    except Exception as ex:
        print(ex)
        return None

def delete_bookmark(id):
    rows_modified = Bookmark.delete().where(Bookmark.id == id).execute() 


