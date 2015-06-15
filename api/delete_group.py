from google.appengine.ext.webapp import template

import webapp2
import json
from models.user import User
from models.link import Link
from models.group import Group
import time
class deleteGroup(webapp2.RequestHandler):
	def get(self):
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user:
			self.error(403)
			self.response.write('No user')
			self.response.write(html)
			return
		group_to_remove= Group.get_by_id(int(self.request.get('groupid')))
		if group_to_remove is None:
			return
		if group_to_remove.admin == user.key:
			group_to_remove.remove_group()
		time.sleep(0.5)
		self.response.set_cookie('our_token', str(user.key.id()))
		self.response.write(json.dumps({'status':'OK'}))
		return

app = webapp2.WSGIApplication([
	('/api/delete_group',deleteGroup)
], debug=True)