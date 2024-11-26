from datetime import datetime

AUTHOR = 'Nicolae CHEDEA'
SITENAME = 'Personal Website of Nicu CHEDEA'
SITEURL = ""
SITELOGO = SITEURL + "/images/nicu.jpg"

PATH = "content"

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ("facebook", "https://www.facebook.com/nicolae.chedea"),
    ("linkedin", "https://www.linkedin.com/in/nicolae-chedea-5a184830/"),
    ("github", "https://github.com/nicolae-chedea"),
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

THEME = "../pelican-themes/Flex"

GITHUB_CORNER_URL = "https://github.com/nicolae-chedea/nicolae-chedea.github.io"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = False
HOME_HIDE_TAGS = True

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = "Nicu CHEDEA"

BROWSER_COLOR = "#0B370B"
PYGMENTS_STYLE = "monokai"