from __future__ import with_statement
from twill.commands import *
from util import *


def login(username):
   "login to a zope site"
   global parser
   with sitecontext():
      add_auth("Zope", "http://" + root, username, parser.get(domain, username))

   
def restart():
   "restart a zope server"
   global parser
   with sitecontext():
      go("http://" + root + "/Control_Panel/manage_main")
      submit(1)

   
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
