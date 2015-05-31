from google.appengine.ext.webapp import template
from operator import itemgetter, attrgetter
import datetime
import operator 
import webapp2
import json
from models.link import Link
from models.user import User

class IndexHandler(webapp2.RequestHandler):
	def get(self):
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
				datatime=link.time_of_enter_the_link
				fromlink=link.from_link
				if fromlink is None:
					urlandlink =[url,des,datatime]
					urls.append(urlandlink)
			template_params['urls'] = urls
		template_params['useremail'] = user.email
		html = template.render("web/templates/mysavedlinks.html", template_params)
		self.response.write(html)
		return

		
class addNewLink(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		description = self.request.get('description')
		url_link = self.request.get('url_link')
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user :
			html = template.render("web/templates/index.html", {})
			self.response.write(html)
			return		
		
		link=Link()
		link.description=description
		link.url_link=url_link
		link.user=user.key
		link.put()
		self.response.set_cookie('our_token', str(user.key.id()))
		self.response.write(json.dumps({'status':'OK'}))
		return 
		
class deleteLink(webapp2.RequestHandler):
	def get(self):
		description = self.request.get('description')
		url_link = self.request.get('url_link')
		from_link = self.request.get('from_link')
		if from_link == 'None':
			from_link=None
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user :
			html = template.render("web/templates/index.html", {})
			self.response.write(html)
			return		
		#link=Link.getLink(user.key,url_link,description,None)
		Link.remove(user.key,url_link,description,from_link)
		self.response.set_cookie('our_token', str(user.key.id()))
		self.response.write(json.dumps({'status':'OK'}))
		return 

class shareLinktootheruser(webapp2.RequestHandler):
	def get(self):
		description = self.request.get('description')
		url_link = self.request.get('url_link')
		to_link = self.request.get('to_link')
		user = None
		if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
			user = User.checkToken(self.request.cookies.get('our_token'))
		if not user :
			html = template.render("web/templates/index.html", {})
			self.response.write(html)
			return
		userTo=User.checkIfUesr(to_link)
		if userTo is None:
			return
		Link.addlinkfronuser(userTo,url_link,description,user)
		self.response.set_cookie('our_token', str(user.key.id()))
		self.response.write(json.dumps({'status':'OK'}))
		return
		
		
		
		
app = webapp2.WSGIApplication([
	('/mysavedlinks', IndexHandler),
	('/addLink', addNewLink),
	('/deletelink',deleteLink),
	('/share',shareLinktootheruser)
], debug=True)
