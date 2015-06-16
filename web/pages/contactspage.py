from google.appengine.ext.webapp import template

import webapp2
from models.user import User
from models.contact import Contact
import json


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
		contactlist= Contact.getAllContactsPerUser(user)
		contacts= []
		if contactlist:
			for contact in contactlist:
				contact_email= contact.contact_user_email
				contact_nickname= contact.nick_name
				email_and_nickname= [contact_email, contact_nickname]
				contacts.append(email_and_nickname)
			template_params['contacts']=contacts
		html = template.render("web/templates/contactspage.html", template_params)
		self.response.write(html)

class addContact(webapp2.RequestHandler):
	def get(self):
		template_params={}
		contact_user_email= self.request.get('contact_user_email')
		nick_name= self.request.get('nick_name')
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user:
			html = template.render("web/templates/index.html", {})
			self.response.write(html)
			return
		userCon= User.checkIfUesr(contact_user_email)
		if userCon is None:
			return
#		contactlist= Contact.getAllContactsPerUser(user)
#		for c in contactlist:
#			if c..contact_user_email is contact_user_email:
#				return
		contact=Contact()
		contact.contact_user_email=contact_user_email
		contact.nick_name=nick_name
		contact.user=user.key
		contact.put()
		self.response.set_cookie('our_token', str(user.key.id()))
		self.response.write(json.dumps({'status':'OK'}))
		return
		
class deleteContact(webapp2.RequestHandler):
	def get(self):
		contact_user_email= self.request.get('contact_user_email')
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user:
			html = template.render("web/templates/index.html", {})
			self.response.write(html)
			return
		Contact.remove(user.key, contact_user_email)
		self.response.set_cookie('our_token', str(user.key.id()))
		self.response.write(json.dumps({'status':'OK'}))
		return

app = webapp2.WSGIApplication([
	('/contactspage', IndexHandler),
	('/addContact', addContact),
	('/deletecontact', deleteContact)
], debug=True)
