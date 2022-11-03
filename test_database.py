import unittest
from unittest import TestCase

import config
config.db_path = 'test_bookmarks.sqlite'

import bookmark_store
from bookmark_store import Bookmark, BookmarkType

class TestDB(TestCase):

    def test_add_bookmark(self):
        Bookmark.delete().execute()
        bookmark_store.add_bookmark(1, '12 Things Every First Timer MUST DO When Visiting NYC !', 'US', 'New York', 'https://www.youtube.com/watch?v=1JJfWnAryrM')
        new_bookmark = Bookmark.select().where(Bookmark.url == 'https://www.youtube.com/watch?v=1JJfWnAryrM').get()
        self.assertEqual(new_bookmark.url, 'https://www.youtube.com/watch?v=1JJfWnAryrM')

    def test_no_duplicate(self):
        Bookmark.delete().execute()
        bookmark_store.add_bookmark(1, '12 Things Every First Timer MUST DO When Visiting NYC !', 'US', 'New York', 'https://www.youtube.com/watch?v=1JJfWnAryrM')
        bookmark_store.add_bookmark(1, '12 Things Every First Timer MUST DO When Visiting NYC !', 'US', 'New York', 'https://www.youtube.com/watch?v=1JJfWnAryrM')
        bookmark_count = Bookmark.select().where(Bookmark.url == 'https://www.youtube.com/watch?v=1JJfWnAryrM').count()
        self.assertEqual(1, bookmark_count)
        bookmark = Bookmark.select().where(Bookmark.url == 'https://www.youtube.com/watch?v=1JJfWnAryrM').get()
        self.assertEqual(bookmark.url, 'https://www.youtube.com/watch?v=1JJfWnAryrM')

    def test_get_bookmarks(self):
        Bookmark.delete().execute()
        bookmark_store.add_bookmark(1, '12 Things Every First Timer MUST DO When Visiting NYC !', 'US', 'New York', 'https://www.youtube.com/watch?v=1JJfWnAryrM')
        bookmark_store.add_bookmark(2, 'Omakase By Korami', 'US', 'New York', 'https://www.yelp.com/biz/omakase-by-korami-new-york?adjust_creative=rviB0Df8WakMZJHruVf0cQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=rviB0Df8WakMZJHruVf0cQ')
        bookmarks = bookmark_store.get_bookmarks()
        self.assertEqual(2, len(bookmarks))




if __name__ == '__main__':
    unittest.main()



