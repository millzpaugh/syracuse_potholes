from .base import *

import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = True 

DATABASES =  {'default': dj_database_url.config()}