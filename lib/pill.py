from ConfigParser import SafeConfigParser as ConfigParser
from twill.commands import *

CONFIG = "config.ini"

config = ConfigParser()
config.read(CONFIG)
go(config.get("global","siteurl"))


def login(username):
   "login to a plone site"
   global config
   go("/login_form")
   formvalue(2,"__ac_name", username)
   formvalue(2,"__ac_password", config.get(username, "password"))
   submit()


def adduser(username, password, emailaddress, fullname=None, mail_me=0):
   "add an user"
   go("/join_form")
   fullname = fullname or username
   formvalue(2, "fullname" fullname)
   formvalue(2, "username", username)
   formvalue(2, "email", emailaddress)
   formvalue(2, "password", password)
   formvalue(2, "password_confirm", password)
   formvalue(2, "mail_me", mail_me)
   submit()

def install(productstring):
   "install a product, given full version string"
   go("/prefs_install_products_form")
   formvalue(2,"products:list", productstring)
   submit()


def uninstall(productstring):
   "uninstall a product, given full version string"
   go("/prefs_install_products_form")
   formvalue(3,"products:list", productstring)
   submit()


def allowmanualpassword():
   go("/reconfig_form")
   formvalue(1,"validate_email",0)
   submit

