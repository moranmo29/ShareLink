from google.appengine.ext.webapp import template

import webapp2
import json
from models.user import User
from models.link import Link
from models.group import Group

class addGroup(webapp2.RequestHandler):
	def get(self):
		template_params={}
		group_name=self.request.get('group_name')
		members= json.loads(self.request.get('members'))
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user:
			self.error(403)
			self.response.write('No user')
			self.response.write(html)
			return
		group= Group()
		group.group_name=group_name
		group.admin= user.key
		for newM in members:
			usermem= User.checkIfUesr(newM)
			group.members.append(usermem.key)
		group.put()
		self.response.set_cookie('our_token', str(user.key.id()))
		self.response.write(json.dumps({'status':'OK'}))
		return

app = webapp2.WSGIApplication([
	('/api/create_group',addGroup)
], debug=True)