from unittest import TestCase

import config
config.db_path = 'test_bookmarks.sqlite'

import bookmark_store
from bookmark_store import Bookmark, BookmarkType

class TestDB(TestCase):

    def test_add_bookmark(self):
        Bookmark.delete().execute()
        bookmark_store.add_bookmark(1, '12 Things Every First Timer MUST DO When Visiting NYC !', 'US', 'New York', 'https://www.youtube.com/watch?v=1JJfWnAryrM')
        new_bookmark_url = Bookmark.select().where(Bookmark.url == 'https://www.youtube.com/watch?v=1JJfWnAryrM').get()
        self.assertEqual(new_bookmark_url, 'https://www.youtube.com/watch?v=1JJfWnAryrM')



