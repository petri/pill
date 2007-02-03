from __future__ import with_statement
from urlparse import urlparse
from contextlib import contextmanager
from ConfigParser import SafeConfigParser as ConfigParser
from twill.commands import *
from twill.namespaces import get_twill_glocals


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
   global parser
   parser.read(filename)

   
def restart():
   "restart a zope server"
   global parser
   with sitecontext():
      add_auth("Zope", "http://" + root, "admin", parser.get(domain,"admin"))
      go("http://" + root + "/Control_Panel/manage_main")
      submit(1)

   

def login(username):
   "login to a plone site"
   global parser
   go("/login_form")
   global_dict, local_dict = get_twill_glocals()
   domain = urlparse(local_dict['__url__']).netloc
   global_dict["domain"] = domain
   global_dict["root"] = parser.get(domain, "zoperoot")
   formvalue(2,"__ac_name", username)
   formvalue(2,"__ac_password", parser.get(domain, username))
   submit()


@silentfailure
def adduser(username, password, emailaddress, fullname=None, mail_me=0):
   "add an user"
   go("/join_form")
   fullname = fullname or username
   formvalue(2, "fullname", fullname)
   formvalue(2, "username", username)
   formvalue(2, "email", emailaddress)
   formvalue(2, "password", password)
   formvalue(2, "password_confirm", password)
   formvalue(2, "mail_me", mail_me)
   submit()


@silentfailure
def install(productstring):
   "install a product, given full version string"
   go("/prefs_install_products_form")
   formvalue(2,"products:list", productstring)
   submit()


@silentfailure
def uninstall(productstring):
   "uninstall a product, given full version string"
   go("/prefs_install_products_form")
   formvalue(3,"products:list", productstring)
   submit()


@silentfailure
def allowmanualpassword():
   go("/reconfig_form")
   formvalue(1,"validate_email",0)
   submit


@silentfailure
def delete(path):
   "delete an object"
   container = '/'.join(path.split('/')[:-1])
   go(container + "/folder_contents")
   formvalue(2, "paths:list", path.split('/')[-1])


def delpropsheet(sheetname):
   "remove a property sheet"
   go("/portal_properties/manage_main")
   formvalue(2,"ids:list", sheetname)
   submit(5)
