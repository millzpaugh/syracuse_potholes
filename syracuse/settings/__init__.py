import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')


try:
  if 'live' in ENVIRONMENT:
    from .live import *
  else:
    from .dev import *
except ImportError:
    pass