from pr0gramm import Api


def test_api_search_find_something():
    pr0_api = Api()
    result = pr0_api.items('awww')
    assert len(result) > 0


def test_api_search_find_nothing():
    pr0_api = Api()
    result = pr0_api.items('awww 1ffe5bfe-2af6-456e-bb43-0595e7792121')

    assert len(result) == 0


def test_api_info():
    pr0_api = Api()
    result = pr0_api.info(3635001)

    assert len(result['tags']) > 0


def test_api_older():
    pr0_api = Api()
    first_fetch = pr0_api.items('awww')

    assert len(first_fetch) > 0

    first_last_post = first_fetch[-1]

    second_fetch = pr0_api.items('awww', older=first_last_post['id'])

    assert len(second_fetch) > 0

    second_last_post = second_fetch[-1]

    assert first_last_post['id'] != second_last_post['id']
