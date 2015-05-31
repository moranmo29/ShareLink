from google.appengine.ext.webapp import template

import webapp2
from models.user import User

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
			template_params['useremail'] = user.email		
		html = template.render("web/templates/details.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/details', IndexHandler)
], debug=True)
