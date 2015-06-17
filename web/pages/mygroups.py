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
		#newlinks
		linkslist=Link.getAllLinksPerUser(user)	
		newurls = []
		template_params = {}
		if linkslist:
			for link in linkslist:
				url = link.url_link
				des = link.description
				fromlink=link.from_link
				if fromlink is not None:
					urlandlink =[url,des,fromlink]
					newurls.append(urlandlink)
			template_params['newurls'] = newurls
		#newlinks
		template_params['useremail'] = user.email
		grouplist= Group.getAllGroups(user)
		groups= []
		if grouplist:
			for group in grouplist:
				group_name= group['group_name']
				groupid=group['id']
				one=[group_name,groupid]
				groups.append(one)
			template_params['groupss']= groups
		html = template.render("web/templates/mygroups.html", template_params)
		self.response.write(html)
		
app = webapp2.WSGIApplication([
	('/mygroups', IndexHandler)
], debug=True)
