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

def get_bookmarks():
    try:
        bookmarks = Bookmark.select()
        return list(bookmarks)
    except Exception as ex:
        print(ex)
        return None

def add_bookmark(type_id, name, country, city, url):
    try:
        new_bookmark = Bookmark(type_id=type_id, name=name, country=country, city=city, url=url)
        result = new_bookmark.save()
        return result
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

def delete_bookmark_by_details(type_id, name, country, city, url):
    try:
        rows_modified = Bookmark.delete().where((Bookmark.type_id == type_id) & (Bookmark.name == name) 
            & (Bookmark.country == country) & (Bookmark.url == url)).execute() 
        return rows_modified
    except Exception as ex:
        print(ex)
        return None

def delete_bookmark_by_id(id):
    try:
        rows_modified = Bookmark.delete().where(Bookmark.id == id).execute() 
        return rows_modified
    except Exception as ex:
        print(ex)
        return None