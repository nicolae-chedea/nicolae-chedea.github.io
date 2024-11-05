AUTHOR = 'Nicolae CHEDEA'
SITENAME = 'Personal Website of Nicu CHEDEA'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
)

# Social widget
SOCIAL = (
    ("Facebook", "https://www.facebook.com/nicolae.chedea"),
    ("LinkedIn", "https://www.linkedin.com/in/nicolae-chedea-5a184830/"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PAGE_ORDER_BY = 'reversed-basename'

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }
