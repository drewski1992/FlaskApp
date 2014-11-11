"""
    config.debug_config
    ~~~~~~~~~~~~~~~~~~~
"""


# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname("run.py"))

print BASE_DIR

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BASE_DIR + "/test.db"
print SQLALCHEMY_DATABASE_URI

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True
CSRF_SESSION_KEY = "1qa!QA2ws@WS3ed#ED4rf$RF"

