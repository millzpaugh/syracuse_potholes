from .base import *

import dj_database_url

DEBUG = True 
TEMPLATE_DEBUG = True 

DATABASES =  {'default': dj_database_url.config()}