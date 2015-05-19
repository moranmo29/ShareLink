#this model keeps the saved links per user
import hashlib

from google.appengine.api import users
from google.appengine.ext import ndb

class User(ndb.Model):
	email= ndb.StringProperty()
	password= ndb.StringProperty()
	
	def checkUser():
		googleuser= users.get_current_user()
		if not googleuser:
			return False
			
		user= User.query(User.email==googleuser.email).get()
		if user:
			passwordMD5=user.password
			if (passwordMD5==User.password):
				return user
		return False
		
	@staticmethod
	def login():
		return users.create_login_url('/MySavedLinks')
		
	@staticmethod
	def logout():
		return users.create_login_url('/')

	@staticmethod
	def connect(password):
		googleUser =users.get_current_user()
		if googleUser:
			user=User.query(User.email == googleUser.email()).get()
			if not user:
				user =User()
				user.emai=googleUser.email()
				user.password=password
				user.put()
			return user
			
		else:
			return "not connected"
	
