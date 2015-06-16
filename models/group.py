from google.appengine.ext import ndb
from user import User
from link import Link

class Group(ndb.Model):
	group_name = ndb.StringProperty()
	admin = ndb.KeyProperty()
	members = ndb.KeyProperty(repeated=True)
	links = ndb.KeyProperty(repeated=True)
	
	@staticmethod
	def getGroup(admin,group_name):
		if not group_name:
			self.error(403)
			self.response.write('Empty group name ')
			return
		
		group=Group.query(Group.admin == admin , Group.group_name == group_name).get()
		if group:
			return group
		return None
		
	def getMembers(self):
		members = []
		for member in self.members:
			members.append({"email":member.get().email})
		return members

	def getLinks(self):
		links = []
		for link in self.links:
			links.append({"email":link.get().user.get().email,"description":link.get().description, "url_link":link.get().url_link,"time_of_enter_the_link":link.get().time_of_enter_the_link})
		return links

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
		
	def remove_group(self):
		for link in self.links:
			link.get().key.delete()
		self.key.delete()
		return
		
	def removeUserFromTheGroup(self,user):
		members = []
		for member in self.members:
			if member.get().key != user.key:
				members.append(member)
		self.members=members
		self.put()
		return