from google.appengine.ext.webapp import template

import webapp2
import json
from models.user import User

class LoginHandler(webapp2.RequestHandler):
	def get(self):
		email = self.request.get('email')
		password = self.request.get('password')
		user = User.query(User.email == email).get()
		if not user or not user.checkPassword(password):
			self.error(403)
			self.response.write('Wrong username or password')
			return

		self.response.set_cookie('our_token', str(user.key.id()))
		self.response.write(json.dumps({'status':'OK'}))
		
		

app = webapp2.WSGIApplication([
	('/login', LoginHandler)
], debug=True)