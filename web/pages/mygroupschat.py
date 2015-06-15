from google.appengine.ext.webapp import template

import webapp2
import json
from models.user import User
from models.link import Link
from models.group import Group

class GroupHandler(webapp2.RequestHandler):
	def get(self, group_id):
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
		if grouplist:
			for group in grouplist:
				group_name= group['group_name']
				groupid=group['id']
				one=[group_name,groupid]
				groups.append(one)
			template_params['groups']= groups
		
		group = Group.get_by_id(int(group_id))
		if group is None:
			return
		if group.admin != user.key and user.key not in group.members:
			template_params['no_access'] = True
			html = template.render('web/templates/mygroups.html', template_params)
			self.response.write(html)
			return
		else:
			template_params['group_name'] = group.group_name
			template_params['group_id'] = group_id
			linksInGroup=group.getLinks()
			links= []
			for link in linksInGroup:
				link_user_name= link['email']
				link_description= link['description']
				link_url_link= link['url_link']
				link_date= link['time_of_enter_the_link']
				one=[link_user_name,link_description,link_url_link,link_date]
				links.append(one)
				links.reverse()
			template_params['links']= links			
			
		html = template.render('web/templates/mygroupschat.html', template_params)
		self.response.write(html)


app = webapp2.WSGIApplication([
	('/mygroups/(.*)', GroupHandler),
], debug=True)
