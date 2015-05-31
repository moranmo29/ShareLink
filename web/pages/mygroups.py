from google.appengine.ext.webapp import template

import webapp2
from models.user import User

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
		html = template.render("web/templates/mygroups.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/mygroups', IndexHandler)
], debug=True)
