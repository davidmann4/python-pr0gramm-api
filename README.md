[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/davidmann4/python-pr0gramm-api) 

# python-pr0gramm-api

[![](https://github.com/ricardoboss/python-pr0gramm-api/workflows/Python%20Unit%20Tests/badge.svg)](https://github.com/ricardoboss/python-pr0gramm-api/actions)

This Python library allows you to search for images on pr0gramm.com: an image board with mostly high quality images, gifs and webms.
Feel free to fork and contribute!

## Example

```python
from pr0gramm import Api

# create API instance
api = Api()
# sfw posts are enabled by default

# query posts which have the tags "awww" and "webm" and at least 100 benis
items = api.items('! s:100 awww webm')

# print the tags associated with the first post
print(api.info(items[0]['id'])['tags'])
```
