from google.appengine.ext.webapp import template

import webapp2
from models.user import User
from models.link import Link

class IndexHandler(webapp2.RequestHandler):
	def get(self):
		template_params = {}
#		user = User.checkUser()
#		if not user:
#			template_params['loginUrl'] = User.loginUrl()
#		else:
#			template_params['logoutUrl'] = User.logoutUrl()
#			template_params['user'] = user.email
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if user:
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
		html = template.render("web/templates/details.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/details', IndexHandler)
], debug=True)
