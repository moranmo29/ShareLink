from google.appengine.ext.webapp import template

import webapp2
from models.user import User
from models.link import Link

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
		linkslist=Link.getAllLinksPerUser(user)	
		#sorted(linkslist, key=lambda link: link.time_of_enter_the_link')   # sort by age
		urls = []
		template_params = {}
		if linkslist:
			for link in linkslist:
				url = link.url_link
				des = link.description
				fromlink=link.from_link
				if fromlink is not None:
					urlandlink =[url,des,fromlink]
					urls.append(urlandlink)
			template_params['urls'] = urls
		template_params['useremail'] = user.email
		html = template.render("web/templates/newlinks.html", template_params)
		self.response.write(html)
		return

		
app = webapp2.WSGIApplication([
	('/newlinks', IndexHandler)
], debug=True)
