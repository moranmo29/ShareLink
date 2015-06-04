from google.appengine.ext.webapp import template

import webapp2
import json
from models.user import User
from models.link import Link
from models.group import Group

class IndexHandler(webapp2.RequestHandler):
	def get(self):
		template_params={}
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user:
			html = template.render("web/templates/index.html", {})
			self.response.write(html)
			return
		template_params['useremail'] = user.email
		group = Group.get_by_id(int(group_id))
		if group.admin != user.key and user.key not in group.members:
			template_params['no_access'] = True
		else:
			template_params['group_name'] = group.group_name
			template_params['group_admin'] = group.admin.get().email
			template_params['group_id'] = group_id
		
		html = template.render("web/templates/mygroups.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/mygroups/(.*)', IndexHandler)
], debug=True)
