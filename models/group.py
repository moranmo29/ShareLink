from google.appengine.ext import ndb
from user import User
from link import Link

class Group(ndb.Model):
	group_name = ndb.StringProperty()
	admin = ndb.KeyProperty()
	members = ndb.KeyProperty(repeated=True)
	links = ndb.KeyProperty(repeated=True)

	def getMembers(self):
		members = []
		for member in self.members:
			members.append({"email":member.get().email})
		return members

#	def getLinks(self):
#		links = []
#		for link in self.links:
#			links.append({"description":member.get().description, "url_link":member.get().url_link})
#		return links

	@staticmethod
	def getGroupsUserAdmin(user):
		q = Group.query(Group.admin == user.key)
		groups_arr = []
		for group in q:
			groups_arr.append({
				"group_name": group.group_name,
				"id": group.key.id(),
				"admin": True
				})
		return groups_arr

	@staticmethod
	def getGroupsUserMember(user):
		q = Group.query(Group.members == user.key)
		groups_arr = []
		for group in q:
			groups_arr.append({
				"group_name": group.group_name,
				"id": group.key.id(),
				"admin": False
			})

		return groups_arr

	@staticmethod
	def getAllGroups(user):
		arr_a = Group.getGroupsUserAdmin(user)
		arr_b = Group.getGroupsUserMember(user)

		return arr_a + arr_b