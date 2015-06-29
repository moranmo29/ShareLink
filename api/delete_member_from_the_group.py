from google.appengine.ext.webapp import template

import webapp2
import json
from models.user import User
from models.link import Link
from models.group import Group
import time
class deleteMemberFromGroup(webapp2.RequestHandler):
	def get(self):
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user:
			self.error(403)
			self.response.write('No user')
			self.response.write(html)
			return
		member = User.checkIfUesr(self.request.get('emailMember'))
		group_to_remove_member= Group.get_by_id(int(self.request.get('groupid')))
		if group_to_remove_member is None:
			return
		if group_to_remove_member.admin == member.key:
			return
		else:
			group_to_remove_member.removeUserFromTheGroup(member)			
		self.response.set_cookie('our_token', str(user.key.id()))
		self.response.write(json.dumps({'status':'OK'}))
		
		return

app = webapp2.WSGIApplication([
	('/api/delete_member_from_the_group',deleteMemberFromGroup)
], debug=True)