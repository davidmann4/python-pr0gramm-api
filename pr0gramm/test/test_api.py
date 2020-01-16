from pr0gramm import Api


def test_api_search_find_something():
    pr0_api = Api()
    result = pr0_api.items("awww")
    assert len(result) != 0


def test_api_search_find_nothing():
    pr0_api = Api()
    result = pr0_api.items("awww 1ffe5bfe-2af6-456e-bb43-0595e7792121")

    assert len(result) == 0


def test_api_info():
    pr0_api = Api()
    result = pr0_api.info(3635001)

    assert len(result['tags']) > 0
