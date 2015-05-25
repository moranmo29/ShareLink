#this model keeps the link
from google.appengine.ext import ndb
from user import User

class Link(ndb.Model):
	user = ndb.KeyProperty(kind=User)
	description = ndb.StringProperty()
	url_link = ndb.StringProperty() #error when write linkproperty
	from_link = ndb.StringProperty()

	@staticmethod
	def getLink(user,link_url,des):
		if not link_url:
			self.error(403)
			self.response.write('Empty url link submitted')
			return
		
		link=Link.query(Link.user == user.key , Link.description == des , Link.url_link == link_url).get()
		if link:
			self.error(402)
			self.response.write('Email taken')
			return
		link=Link()
		link.user=user.key
		link.url_link=link_url
		link.description=des
		link.put()
		return link
		
	@staticmethod
	def getAllLinksPerUser(user):
		links=Link.query(Link.user == user.key )
		return links

	def remove(self):
		link=Link.query(Link.user == self.user.key ,Link.url_link == self.url , Link.description == self.des )
		Link.remove(link);
		return
