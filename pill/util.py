from __future__ import with_statement
from urlparse import urlparse
from contextlib import contextmanager
from ConfigParser import SafeConfigParser as ConfigParser
from twill.commands import *
from twill.namespaces import get_twill_glocals

__all__ = ("parser", "sitecontext", "silentfailure", "load")

CONFIG = "config.ini"
parser = ConfigParser()

try:
   parser.read(CONFIG)
except:
   pass


@contextmanager
def sitecontext():
   "set the site context"
   global parser
   g = globals()
   tg, tl = get_twill_glocals()
   g.update(tg)
   yield
   for k in tg:
      del g[k]


def silentfailure(func):

   def wrapper(*args, **kwargs):
      if "silent" in args:
        try:
           return func(*args, **kwargs)
        except:
           pass
      else:
         return func(*args, **kwargs)

   return wrapper


def load(filename=CONFIG):
   "load a config file"
   global parser
   parser.read(filename)
