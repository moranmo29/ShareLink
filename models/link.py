#this model keeps the link
from google.appengine.ext import ndb
from user import User
import datetime
import time
class Link(ndb.Model):
	user = ndb.KeyProperty()
	description = ndb.StringProperty()
	url_link = ndb.StringProperty() #error when write linkproperty
	from_link = ndb.StringProperty()
	time_of_enter_the_link=ndb.DateTimeProperty(auto_now_add=True)
	ifInTheGroup=ndb.BooleanProperty(default=False)
	
	@staticmethod
	def getLink(user,link_url,des,from_link):
		if not link_url:
			self.error(403)
			self.response.write('Empty url link submitted')
			return
		
		link=Link.query(Link.user == user , Link.description == des , Link.url_link == link_url , Link.from_link==from_link).get()
		if link:
			return link
		return None
		
	@staticmethod
	def getAllLinksPerUser(user):
		links=[]
		qur=Link.query(Link.user == user.key ).order(-Link.time_of_enter_the_link)
		if qur:
			for url_link in qur:
				links.append(url_link)
			return links
		return None
	
	@staticmethod
	def remove(user,link_url,des,from_link):
		if from_link == "None" :
			link=Link.getLink(user,link_url,des,None)
		link=Link.getLink(user,link_url,des,from_link)		
		if link is not None:
			if link.ifInTheGroup is False:
				link.key.delete();
		return
		
	@staticmethod
	def addlinkfronuser(user,link_url,des,fromuser):
		link=Link()
		link.description=des
		link.url_link=link_url
		link.user=user.key
		link.from_link=fromuser.email
		link.put()
		return
