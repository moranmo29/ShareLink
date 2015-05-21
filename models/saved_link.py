<<<<<<< HEAD
#this model keeps the link
=======
#this model keeps the link per user
>>>>>>> origin/master

from google.appengine.ext import ndb
from user import User

class Link(ndb.Model):

    description = ndb.StringProperty()
    url_link = ndb.LinkProperty()
    from_link = ndb.StringProperty()
    user = ndb.KeyProperty(kind= User)

    @staticmethod
    def checkTokenLink(token):
        link = Link.get_bu_id(long(token))
        return link

    def setDescription(self,des):
        self.description = des
        self.put()


    @staticmethod
    def setLink(des,url,user):
        link=Link.query(Link.user == user.key ,Link.url_link == url , Link.description == des ).get()
        if link is None and user.key is not None and (url.text()!=0):
            link.description=des
            link.url_link = url
            link.from_link = ""
            link.put()
        return link;

    def setFromLink(self,fromlink):
        self.from_link = fromlink
        self.put()

    @staticmethod
    def getAllLinksPerUser(user):
         links=Link.query(Link.user == user.key )
         return links


    @staticmethod
    def getLink(url,des,user):
        link=Link.query(Link.user == user.key ,Link.url_link == url , Link.description == des ).get()
        return link

    def remove(self):
        link=Link.query(Link.user == self.user.key ,Link.url_link == self.url , Link.description == self.des )
        Link.remove(link);
        return
