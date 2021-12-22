from lab11.zad3.FriendShips import FriendShips
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = FriendShips()

    def test_assert_that_init_object_is_dict(self):
        self.assertEqual(type(self.temp.friendships), dict)

    def test_assert_that_init_object_is_empty_dict(self):
        self.assertEqual(len(self.temp.friendships), 0)

    def test_assert_add_friend_value_is_list(self):
        self.temp.add_friend("me", "you")
        self.assertEqual(type(self.temp.friendships['me']), list)

    def test_assert_raises_add_friend_is_int(self):
        self.assertRaises(TypeError, self.temp.add_friend, "kk", 5)

    def test_assert_raises_add_friend_is_none(self):
        self.assertRaises(TypeError, self.temp.add_friend, "kk", None)

    def test_assert_raises_add_friend_is_list(self):
        self.assertRaises(TypeError, self.temp.add_friend, "kk", ["kkk"])

    def test_assert_raises_add_friend_is_bool(self):
        self.assertRaises(TypeError, self.temp.add_friend, "kk", True)

    def test_assert_raises_add_friend_person_is_int(self):
        self.assertRaises(TypeError, self.temp.add_friend, 5, "ll")

    def test_assert_raises_add_friend_person_is_none(self):
        self.assertRaises(TypeError, self.temp.add_friend, None, "ll")

    def test_assert_raises_add_friend_person_is_list(self):
        self.assertRaises(TypeError, self.temp.add_friend, ["kkk"], "ll")

    def test_assert_raises_add_friend_person_is_bool(self):
        self.assertRaises(TypeError, self.temp.add_friend, True, "ll")

    def test_assert_add_friend(self):
        self.temp.add_friend("me", "you")
        self.assertEqual(self.temp.friendships, {'me': ['you']})

    def test_assert_add_2_friends(self):
        self.temp.add_friend("me", "you")
        self.temp.add_friend("he", "she")
        self.assertEqual(self.temp.friendships, {'me': ['you'], 'he': ['she']})

    def test_assert_raises_make_friends_is_int(self):
        self.assertRaises(TypeError, self.temp.make_friends, "kk", 5)

    def test_assert_raises_make_friends_is_none(self):
        self.assertRaises(TypeError, self.temp.make_friends, "kk", None)

    def test_assert_raises_make_friends_is_list(self):
        self.assertRaises(TypeError, self.temp.make_friends, "kk", ["kkk"])

    def test_assert_raises_make_friends_is_bool(self):
        self.assertRaises(TypeError, self.temp.make_friends, "kk", True)

    def test_assert_raises_make_friends_person_is_int(self):
        self.assertRaises(TypeError, self.temp.make_friends, 5, "ll")

    def test_assert_raises_make_friends_person_is_none(self):
        self.assertRaises(TypeError, self.temp.make_friends, None, "ll")

    def test_assert_raises_make_friends_person_is_list(self):
        self.assertRaises(TypeError, self.temp.make_friends, ["kkk"], "ll")

    def test_assert_raises_make_friends_person_is_bool(self):
        self.assertRaises(TypeError, self.temp.make_friends, True, "ll")

    def test_assert_make_friends(self):
        self.temp.make_friends("me", "you")
        self.assertEqual(self.temp.friendships, {'me': ['you'], "you": ["me"]})

    def test_assert_make_2_friends(self):
        self.temp.make_friends("me", "you")
        self.temp.make_friends("he", "she")
        self.assertEqual(self.temp.friendships, {'me': ['you'], "you": ["me"], 'he': ['she'], "she": ['he']})


    def test_assert_raises_get_friends_list_person_is_int(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, 5)

    def test_assert_raises_get_friends_list_person_is_none(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, None)

    def test_assert_raises_get_friends_list_person_is_list(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, ["kkk"])

    def test_assert_raises_get_friends_list_person_is_bool(self):
        self.assertRaises(TypeError, self.temp.getFriendsList, True)

    def test_assert_raises_get_friends_list_unknown_person(self):
        self.temp.add_friend("me", "you")
        self.assertRaises(ValueError, self.temp.getFriendsList, "smb")

    def test_assert_raises_get_friends_list_unknown_person_swapped(self):
        self.temp.add_friend("me", "you")
        self.assertRaises(ValueError, self.temp.getFriendsList, "you")

    def test_assert_get_friends_basic(self):
        self.temp.add_friend("me", "you")
        self.assertEqual(self.temp.getFriendsList('me'), ['you'])
    
    def test_assert_get_friends_10(self):
        for x in range(10):
            self.temp.add_friend("me", "you")
        self.assertEqual(self.temp.getFriendsList('me'), ['you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you', 'you'])
        
    def test_assert_get_friends_100(self):
        for x in range(100):
            self.temp.add_friend("me", "you")
        self.assertEqual(self.temp.getFriendsList('me'), ['you' for x in range(100)])


    def test_assert_raises_are_friends_is_int(self):
        self.assertRaises(TypeError, self.temp.areFriends, "kk", 5)

    def test_assert_raises_are_friends_is_none(self):
        self.assertRaises(TypeError, self.temp.areFriends, "kk", None)

    def test_assert_raises_are_friends_is_list(self):
        self.assertRaises(TypeError, self.temp.areFriends, "kk", ["kkk"])

    def test_assert_raises_are_friends_is_bool(self):
        self.assertRaises(TypeError, self.temp.areFriends, "kk", True)

    def test_assert_raises_are_friends_person_is_int(self):
        self.assertRaises(TypeError, self.temp.areFriends, 5, "ll")

    def test_assert_raises_are_friends_person_is_none(self):
        self.assertRaises(TypeError, self.temp.areFriends, None, "ll")

    def test_assert_raises_are_friends_person_is_list(self):
        self.assertRaises(TypeError, self.temp.areFriends, ["kkk"], "ll")

    def test_assert_raises_are_friends_person_is_bool(self):
        self.assertRaises(TypeError, self.temp.areFriends, True, "ll")


    def test_assert_raises_are_friends_unknown_person(self):
        self.temp.add_friend("me", "you")
        self.assertRaises(ValueError, self.temp.areFriends, "you", "wrong")

    def test_assert_raises_are_friends_unknown_person_swapped(self):
        self.temp.add_friend("me", "you")
        self.assertRaises(ValueError, self.temp.areFriends, "wrong", "you")

    def test_assert_are_friends_positive(self):
        self.temp.add_friend("me", "you")
        self.assertEqual(self.temp.areFriends("you", "me"), True)

    def test_assert_are_friends_negative(self):
        self.temp.add_friend("me", "you")
        self.assertEqual(self.temp.areFriends("she", "me"), False)





