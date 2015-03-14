__author__ = 'mojtaba.banaie'
from Handlers.index_handler import IndexHandler
from Handlers.category__handler import CategoryHandler,CategoryEditHandler,CategoryDeleteHandler,CategoryNewHandler
from Handlers.search_handler import SearchHandler,SearchShowHandler
from Handlers.news_handler import NewsHandler,NewsNewHandler,NewsEditHandler,NewsDeleteHandler

urlList  = [
    (r'/', IndexHandler),
    (r'/category$', CategoryHandler),
    (r'/category/edit/(\d+)$', CategoryEditHandler),
    (r'/category/delete/(\d+)$', CategoryDeleteHandler),
    (r'/category/new$', CategoryNewHandler),
    (r'/news$', NewsHandler),
    (r'/news/edit/(\d+)$', NewsEditHandler),
    (r'/news/delete/(\d+)$', NewsDeleteHandler),
    (r'/news/new$', NewsNewHandler),
    (r'/search$',SearchHandler),
    (r'/showsearch$',SearchShowHandler)
]