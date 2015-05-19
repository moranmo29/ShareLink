#this model keeps the saved links per user

from google.appengine.ext import ndb

from user import User

class SavedLink(ndb.Model):
	url = ndb.LinkProperty()
	description= ndb.StringProperty()
	user= ndb.KeyProperty(kind=User)
	
	@staticmethod
	def newLink(userNew, urlNew, descriptionNew=""): #add link, if succeed returns the link, else return NONE
		link=SavedLink.query(SavedLink.user==user.key, SavedLink.url== url, SavedLink.description== description).get()
		if link is None and user.key is not None and url is not None:
			link.url= urlNew
			link.description= descriptionNew
			link.user= userNew.key
			link.put()
			return link
		return None
	
	@staticmethod	
	def allLinkPerUser(user): 
		return SavedLink.query(user.key==SavedLink.user)

	def changeDescription(self, newDescription):
		self.description= newDescription
		self.put()
		return True
	
	@staticmethod	
	def getLink(user, description, url):
		link= SavedLink.query(SavedLink.user==user.key, SavedLink.url== url, SavedLink.description== description).get()
		
	@staticmethod
	def removeLink(userNew, urlNew, descriptionNew=""): #add link, if succeed returns the link, else return NONE
		link=SavedLink.query(SavedLink.user==user.key, SavedLink.url== url, SavedLink.description== description).get()
		if link is not None :
			link.delete()
			return True
		return False