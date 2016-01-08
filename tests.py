import unittest
import pr0gramm

class TestStringMethods(unittest.TestCase):
    def test_API_search_find_something(self):
        pr0_api = pr0gramm.Api()
        result = pr0_api.search("awww")
        self.assertTrue(len(result)!=0)

    def test_API_search_find_nothing(self):
        pr0_api = pr0gramm.Api()
        result = pr0_api.search("awww 1ffe5bfe-2af6-456e-bb43-0595e7792121")
        self.assertTrue(len(result)==0)


if __name__ == '__main__':
    unittest.main()
