#this model keeps the link
from google.appengine.ext import ndb
from user import User
class Contact(ndb.Model):
	user = ndb.KeyProperty(kind=User)
	contact_user_email = ndb.StringProperty() #mail?
	nick_name = ndb.StringProperty()

	@staticmethod
	def getContact(user, contact_user_email):
		contact=Contact.query(Contact.user == user , Contact.contact_user_email == contact_user_email).get()
		if contact:
			return contact
		return None
		
	@staticmethod
	def getAllContactsPerUser(user):
		contacts=[]
		qur=Contact.query(Contact.user == user.key )#.order(-Link.time_of_enter_the_link)
		if qur:
			for contact_user_email in qur:
				contacts.append(contact_user_email)
			return contacts
		return None
	
	@staticmethod
	def remove(user, contact_user_email):
		contact=Contact.getContact(user, contact_user_email)		
		#link=Link.query(Link.user == user , Link.description == des , Link.url_link == link_url , Link.from_link==None).get()
		if contact is not None:
			contact.key.delete();
		return
		
	@staticmethod
	def addcontactfromuser(user, contact_user_email, nick_name):
		contact=Contact()
		contact.contact_user_email=contact_user_email
		contact.nick_name=nick_name
		contact.user=user.key
		contact.put()
		return
