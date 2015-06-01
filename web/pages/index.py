from google.appengine.ext.webapp import template
from google.appengine.api import mail
import json
import webapp2
import string
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
		html = template.render("web/templates/index.html", template_params)
		self.response.write(html)

class SendMail(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		mailfrom = self.request.get('mailfrom')
		to = self.request.get('to')
		if not mail.is_email_valid(to):
			return
		url_link = self.request.get('url_link')
		description = self.request.get('description')
		mail.send_mail(sender="sharelink2015.appspot.com <adi8554@gmail.com>",
						to=to+"<"+to+">",
						subject="Hey, your friend "+ mailfrom+ " thought you would like to watch this link",
						body="""
Hello """+to+""":
Your friend would like that you see the next link:
"""+url_link+""".
"""+description+"""
______________________________________________________________________________________
If you send a lot of links so our site may interest you: www.sharelink2015.appspot.com.
The sharelink Team.
""")
		self.response.write(json.dumps({'status':'OK'}))
app = webapp2.WSGIApplication([
	('/sendmail',SendMail),
	('/index', IndexHandler),
	('/', IndexHandler)
], debug=True)
