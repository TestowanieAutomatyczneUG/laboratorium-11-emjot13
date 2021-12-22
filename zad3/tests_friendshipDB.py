from lab11.zad3.friendshipsDB import FriendshipsDB
import unittest
from unittest.mock import MagicMock

class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = FriendshipsDB()

    def test_database_add_friend(self):
        self.temp.database.add_friend = MagicMock()
        self.temp.add_friend(("me", "me"), "you")
        self.temp.database.add_friend.assert_called_with(("me", "me"), "you")

    def test_database_add_friend2(self):
        self.temp.database.add_friend = MagicMock()
        self.temp.add_friend("me", "he")
        self.temp.database.add_friend.assert_called_with("me", "he")

    def test_database_add_friend3(self):
        self.temp.database.add_friend = MagicMock()
        self.temp.add_friend(True, "she")
        self.temp.database.add_friend.assert_called_with(True, "she")

    def test_add_friend_raise_type_error_int(self):
        self.temp.database.add_friend = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.add_friend, 3, 2)
        self.temp.database.add_friend.assert_called_with(3, 2)

    def test_add_friend_raise_type_error_list(self):
        self.temp.database.add_friend = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.add_friend, ["ala"], ["kasia"])
        self.temp.database.add_friend.assert_called_with(["ala"], ["kasia"])

    def test_add_friend_raise_type_error_dict(self):
        self.temp.database.add_friend = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.add_friend, {"ala": "ma"}, {"kota": "!"})
        self.temp.database.add_friend.assert_called_with({"ala": "ma"}, {"kota": "!"})

    def test_add_friend_raise_type_error_none(self):
        self.temp.database.add_friend = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.add_friend, None, None)
        self.temp.database.add_friend.assert_called_with(None, None)

    def test_add_friend_unknown_person(self):
        self.temp.database.add_friend = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.add_friend, 'annonymous', 'person2')
        self.temp.database.add_friend.assert_called_with('annonymous', 'person2')

    def test_database_make_friends(self):
        self.temp.database.make_friends = MagicMock()
        self.temp.make_friends(None, "you")
        self.temp.database.make_friends.assert_called_with(None, "you")

    def test_database_make_friends2(self):
        self.temp.database.make_friends = MagicMock()
        self.temp.make_friends("me", [])
        self.temp.database.make_friends.assert_called_with("me", [])

    def test_database_make_friends3(self):
        self.temp.database.make_friends = MagicMock()
        self.temp.make_friends(5, "she")
        self.temp.database.make_friends.assert_called_with(5, "she")

    def test_make_friends_raise_type_error_int(self):
        self.temp.database.make_friends = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.make_friends, 3, 2)
        self.temp.database.make_friends.assert_called_with(3, 2)


    def test_make_friends_raise_type_error_list(self):
        self.temp.database.make_friends = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.make_friends, ["ala"], ["kasia"])
        self.temp.database.make_friends.assert_called_with(["ala"], ["kasia"])

    def test_make_friends_raise_type_error_dict(self):
        self.temp.database.make_friends = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.make_friends, {"ala": "ma"}, {"kota": "!"})
        self.temp.database.make_friends.assert_called_with({"ala": "ma"}, {"kota": "!"})

    def test_make_friends_raise_type_error_none(self):
        self.temp.database.make_friends = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.make_friends, None, None)
        self.temp.database.make_friends.assert_called_with(None, None)

    def test_make_friends_unknown_person(self):
        self.temp.database.make_friends = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.make_friends, 'annonymous', 'person2')
        self.temp.database.make_friends.assert_called_with('annonymous', 'person2')

    def test_database_getFriendsList(self):
        self.temp.database.getFriendsList = MagicMock()
        self.temp.getFriendsList(("me", "me"))
        self.temp.database.getFriendsList.assert_called_with(("me", "me"))

    def test_database_getFriendsList2(self):
        self.temp.database.getFriendsList = MagicMock()
        self.temp.getFriendsList("me")
        self.temp.database.getFriendsList.assert_called_with("me")

    def test_database_getFriendsList3(self):
        self.temp.database.getFriendsList = MagicMock()
        self.temp.getFriendsList(True)
        self.temp.database.getFriendsList.assert_called_with(True)

    def test_getFriendsList_raise_type_error_int(self):
        self.temp.database.getFriendsList = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.getFriendsList, 3)
        self.temp.database.getFriendsList.assert_called_with(3)


    def test_getFriendsList_raise_type_error_list(self):
        self.temp.database.getFriendsList = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.getFriendsList, ["ala"])
        self.temp.database.getFriendsList.assert_called_with(["ala"])

    def test_getFriendsList_raise_type_error_dict(self):
        self.temp.database.getFriendsList = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.getFriendsList, {"ala": "ma"})
        self.temp.database.getFriendsList.assert_called_with({"ala": "ma"})

    def test_getFriendsList_raise_type_error_none(self):
        self.temp.database.getFriendsList = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.getFriendsList, None)
        self.temp.database.getFriendsList.assert_called_with(None)

    def test_getFriendsList_unknown_person(self):
        self.temp.database.getFriendsList = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.getFriendsList, 'annonymous')
        self.temp.database.getFriendsList.assert_called_with('annonymous')

    def test_areFriends_raise_type_error_int(self):
        self.temp.database.areFriends = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.areFriends, 3, 2)
        self.temp.database.areFriends.assert_called_with(3, 2)


    def test_areFriends_raise_type_error_list(self):
        self.temp.database.areFriends = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.areFriends, ["ala"], ["kasia"])
        self.temp.database.areFriends.assert_called_with(["ala"], ["kasia"])

    def test_areFriends_raise_type_error_dict(self):
        self.temp.database.areFriends = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.areFriends, {"ala": "ma"}, {"kota": "!"})
        self.temp.database.areFriends.assert_called_with({"ala": "ma"}, {"kota": "!"})

    def test_areFriends_raise_type_error_none(self):
        self.temp.database.areFriends = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.areFriends, None, None)
        self.temp.database.areFriends.assert_called_with(None, None)

    def test_areFriends_unknown_person(self):
        self.temp.database.areFriends = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.areFriends, 'annonymous', 'person2')
        self.temp.database.areFriends.assert_called_with('annonymous', 'person2')


