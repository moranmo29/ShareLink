from google.appengine.ext.webapp import template
from google.appengine.api import mail
import json

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
			template_params['useremail'] = user.email	
			#newlinks
		html = template.render("web/templates/contactuspage.html", template_params)
		self.response.write(html)

class sendMailContactUs(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		mailfrom = self.request.get('mailfrom')
		name = self.request.get('name')
		message = self.request.get('message')
		if not mail.is_email_valid(mailfrom):
			return
		mail.send_mail(sender="sharelink2015.appspot.com <adi8554@gmail.com>",
						to="sharelink.contact@gmal.com<sharelink.contact@gmail.com>",
						subject="USER CONTACT US",
						body="""
FROM: """+name+"""
MAIL: """+mailfrom+"""

"""+message+"""
______________________________________________________________________________________
The sharelink Team. www.sharelink2015.appspot.com.
""")
		self.response.write(json.dumps({'status':'OK'}))


app = webapp2.WSGIApplication([
	('/contactuspage', IndexHandler),
	('/sendcontactus',sendMailContactUs)
], debug=True)
