from lab11.zad3.FriendShips import FriendShips


class FriendshipsDB:
    def __init__(self):
        self.database = FriendShips()

    def add_friend(self, person1, person2):
        return self.database.add_friend(person1, person2)

    def make_friends(self, person1, person2):
        return self.database.make_friends(person1, person2)

    def getFriendsList(self, person):
        return self.database.getFriendsList(person)

    def areFriends(self, person1, person2):
        return self.database.areFriends(person1, person2)

