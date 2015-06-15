from google.appengine.ext.webapp import template

import webapp2
import json
from models.user import User

class CheckMember(webapp2.RequestHandler):
	def get(self):
		member=self.request.get('member')
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user:
			self.error(403)
			self.response.write('No user')
			self.response.write(html)
			return
		if (user.email==member):
			return
		mem=User.checkIfUesr(member)
		if mem is None:
			return
		self.response.set_cookie('our_token', str(user.key.id()))
		self.response.write(json.dumps({'status':'OK'}))
		return

app = webapp2.WSGIApplication([
	('/api/add_memebr',CheckMember)
], debug=True)