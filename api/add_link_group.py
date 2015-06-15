from google.appengine.ext.webapp import template

import webapp2
import json
from models.user import User
from models.link import Link
from models.group import Group

class addLinkToTheGroup(webapp2.RequestHandler):
	def get(self):
		des=self.request.get('des')
		url_link=self.request.get('url_link')
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user:
			self.error(403)
			self.response.write('No user')
			self.response.write(html)
			return
		group = Group.get_by_id(int(self.request.get('groupid')))
		link=Link()
		link.description=des
		link.url_link=url_link
		link.user=user.key
		link.ifInTheGroup=True
		link.put()
		group.links.append(link.key)
		group.put()
		self.response.write(json.dumps({"status": "OK"}))


app = webapp2.WSGIApplication([
	('/api/add_link_group',addLinkToTheGroup)
], debug=True)