from google.appengine.ext.webapp import template
import webapp2
import json
from models.user import User

class MainHandler(webapp2.RequestHandler):
	def get(self):
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token')) 

		template_variables = {}
		if user: #CHECK IF THER IS USER
			template_variables['user'] = user.email

		html = template.render('templates/index.html', template_variables)
		self.response.write(html)

class LoginHandler(webapp2.RequestHandler):
	def get(self):
		email = self.request.get('email')
		password = self.request.get('password')
		user = User.query(User.email == email).get() #check that its an unique email address
		if not user or not user.checkPassword(password):
			self.error(403) #wrong password retruns error
			self.response.write('Wrong username or password')
			return
# if everything ok we go on
		self.response.set_cookie('our_token', str(user.key.id())) # 'ok cookie'
		self.response.write(json.dumps({'status':'OK'})) # 'ok status'

		#signup!
class RegisterHandler(webapp2.RequestHandler):
	def get(self):
		email = self.request.get('email') #gets email
		password = self.request.get('password') #gets password
		if not password:
			self.error(403)
			self.response.write('Empty password submitted')
			return

		user = User.query(User.email == email).get()
		if user:
			self.error(402)
			self.response.write('Email taken') #email already taken 
			return

		user = User() # create user
		user.email = email #enter email
		user.setPassword(password) #enter password
		user.put() # enter to the database/datestore
		self.response.set_cookie('our_token', str(user.key.id())) #cookies
		self.response.write(json.dumps({'status':'OK'})) 

class LogoutHandler(webapp2.RequestHandler): ##############################################################
	def get(self):
		self.response.delete_cookie('our_token')
		self.redirect('/')

#class PersonalHandler(webapp2.RequestHandler):
#    def get(self):
#        user = None
#		# we decide eize name to put here down
#        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
#            user = User.checkToken(self.request.cookies.get('our_token')) 
#
#        if not user:
#            self.redirect('/')

#        html = template.render('templates/personal.html', {})
#        self.response.write(html)

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/login', LoginHandler),
	('/register', RegisterHandler),
	('/logout', LogoutHandler)#,#('/personal', PersonalHandler)
], debug=True)
