class FriendShips:

    def __init__(self):
        self.friendships = {}

    def add_friend(self, person, friend):
        if type(person) is not str or type(friend) is not str:
            raise TypeError
        if person not in self.friendships.keys():
            friends_list = [friend]
            self.friendships[person] = friends_list
        else:
            self.friendships[person].append(friend)

    def make_friends(self, person1, person2):
        self.add_friend(person1, person2)
        self.add_friend(person2, person1)

    def getFriendsList(self, person):
        if type(person) is not str:
            raise TypeError
        elif person not in self.friendships.keys():
            raise ValueError
        return self.friendships[person]

    def areFriends(self, person1, person2):
        if type(person1) is not str or type(person2) is not str:
            raise TypeError
        elif person2 not in self.friendships.keys():
            raise ValueError
        return person1 in self.friendships[person2]


# obj = FriendShips()
# # obj.add_friend("me", "you")
# # obj.add_friend("me", "you1")
# # obj.add_friend("he", "you")
# obj.make_friends("me", "you")
# print(obj.areFriends("me", "you"))
#
# print(obj.getFriendsList("me"))
# print(obj.friendships)
