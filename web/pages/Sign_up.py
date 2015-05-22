from google.appengine.ext.webapp import template

import webapp2

class IndexHandler(webapp2.RequestHandler):
	def get(self):
		template_params = {}
#		email = self.request.get('email')
#		password = self.request.get('password')
#		if not password:
#			self.error(403)
#			self.response.write('Empty password submitted')
#			return
			
#		user = User.query(User.email == email).get()
#		if user:
#			self.error(402)
#			self.response.write('Email taken')
#			return

#		user = User()
#		user.email = email
#		user.setPassword(password)
#		user.put()
#		self.response.set_cookie('our_token', str(user.key.id()))
#		self.response.write(json.dumps({'status':'OK'}))
		
		html = template.render("web/templates/sign_up.html", template_params)
		self.response.write(html)


app = webapp2.WSGIApplication([
	('/sign_up', IndexHandler)
], debug=True)

