from __future__ import with_statement
from urlparse import urlparse
from contextlib import contextmanager
from ConfigParser import SafeConfigParser as ConfigParser
from twill.commands import *
from twill.namespaces import get_twill_glocals

from util import *


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


class config:

   def __init__(self, method, param):
      getattr(self, method)(param)
      
   @silentfailure
   def setpassword(self,param):
      go("/reconfig_form")
      if param == "allow":
         formvalue(2,"validate_email","0")
      else:
         formvalue(2, "validate_email", "1")
         
      submit()


def delpropsheet(sheetname):
   "remove a property sheet"
   go("/portal_properties/manage_main")
   formvalue(2,"ids:list", sheetname)
   submit(5)
