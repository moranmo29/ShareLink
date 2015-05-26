from google.appengine.ext.webapp import template

import webapp2
import json
import smtplib
from models.link import Link
from models.user import User

class shareMailHandler(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		description = self.request.get('description')
		url_link = self.request.get('url_link')
		email = self.request.get('email')
		
		sender= 'sharelink.contact@gmail.com'
		reciever= [email] #is that ok?
		
		message= "hello, this is a message that sent to you from Sharelink:\n"
		message.join(url_link)
		message.join("\n")
		message.join(description)
		
		try:
			smtpObj = smtplib.SMTP('localhost')
			smtpObj.sendmail(sender, reciever, message)
			print "successfully sent mail"
		except SMTPException:
			print "Error: unable to send mail"
#		user = None
#		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
#			user = User.checkToken(self.request.cookies.get('our_token'))
#		if not user :
#			html = template.render("web/templates/index.html", {})
#			self.response.write(html)
#			return		
#		
#		link=Link()
#		link.description=description
##		link.url_link=url_link
#		link.user=user.key
#		link.put()
#		self.response.set_cookie('our_token', str(user.key.id()))
#		self.response.write(json.dumps({'status':'OK'}))
#		return 

		


app = webapp2.WSGIApplication([
	('/shareMail', shareMailHandler)
], debug=True)
