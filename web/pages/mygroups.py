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
		grouplist= Group.getAllGroups(user)
		groups= []
#		if grouplist:
#			for group in grouplist:
#				group_name= group.group_name
#				admin= group.admin
#				groupandadmin=[group_name, admin]
#				groups.append(groupandadmin)
#			template_params['groups']= groups

#		group = Group.get_by_id(int(group_id))
#		if group.admin != user.key and user.key not in group.members:
#			template_params['no_access'] = True
#		else:
#			template_params['group_name'] = group.group_name
#			template_params['group_admin'] = group.admin.get().email
#			template_params['group_id'] = group_id
		
		html = template.render("web/templates/mygroups.html", template_params)
		self.response.write(html)

class addGroup(webapp2.RequestHandler):
	def get(self):
		template_params={}
		group_name=self.request.get('group_name')
		members= json.loads(self.request.get('members'))
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user:
			html = template.render("web/templates/index.html", {})
			self.response.write(html)
			return
		template_params['useremail'] = user.email
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
	('/mygroups', IndexHandler),
	('/addGroup',addGroup)
], debug=True)
