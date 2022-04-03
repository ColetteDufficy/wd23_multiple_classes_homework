import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Winkie", 50, "Wannabe")
        self.guest2 = Guest("Leigh", 40, "Business Time")
        self.guest3 = Guest("Becky", 20, "Let it Go")
        self.guest4 = Guest("Erica", 5, "Maneater")
        
        self.room1 = Room("Blue Room", 7, 100, 12.99)
        self.room2 = Room("Green Room", 3, 50, 12.99)
        
        self.song1 = Song("Spice Girls", "Wannabe")
        self.song2 = Song("Mr Brightside", "The Killers")
        
    def test_room_has_name(self):
        self.assertEqual("Blue Room", self.room1.room_name)
        
    def test_check_room_max_capacity(self):
        self.assertEqual(3, self.room2.max_capacity)
        
    def test_room_till_total(self):
        self.assertEqual(50, self.room2.till)
        
    def test_number_of_guests_in_empty_room(self):
        self.assertEqual(0, self.room1.head_count())
        
    def test_entry_fee(self):
        self.assertEqual(12.99, self.room1.entry_fee)
        
    def test_check_in_guest(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_in(self.guest3)
        self.assertEqual(3, self.room1.head_count())
        
    def test_check_out_guest(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_out(self.guest2)
        self.assertEqual(1, self.room1.head_count())
    
    def test_add_song_to_playlist(self):
        self.room1.add_song_to_playlist(self.song1)
        self.assertEqual("Wannabe", self.song1.title)
        
    def test_room_has_capacity1__there_is_room(self):
        self.assertEqual(f"Welcome to {self.room2.room_name}!", self.room2.room_has_capacity(self))
        self.assertEqual(1, self.room2.head_count())
        
    def test_room_has_capacity2__there_is_room(self):
        self.room2.room_has_capacity(self)
        self.assertEqual(f"Welcome to {self.room2.room_name}!", self.room2.room_has_capacity(self))
        self.assertEqual(2, self.room2.head_count())

    def test_room_has_capacity3__there_is_room(self):
        self.room2.room_has_capacity(self)
        self.room2.room_has_capacity(self)
        self.assertEqual(f"Welcome to {self.room2.room_name}!", self.room2.room_has_capacity(self))
        self.assertEqual(3, self.room2.head_count())
        
    def test_room_has_capacity4__there_is_no_room(self):
        self.room2.room_has_capacity(self)
        self.room2.room_has_capacity(self)
        self.room2.room_has_capacity(self)
        self.assertEqual(f"Sorry, the {self.room2.room_name} is full", self.room2.room_has_capacity(self))
        self.assertEqual(3, self.room2.head_count())
        
    def test_charging_entry_fee(self):
        self.assertEqual(112.99, self.room1.charge_entry_fee(self.guest1))
        
        
    def test_guest_favourite_song__yes_on_playlist(self):
        self.room1.add_song_to_playlist(self.song1)
        self.assertEqual("Whoo hoo!", self.room1.favourite_song_on_playlist(self.guest1.fav_song, self.guest1))
    
    def test_guest_favourite_song__not_on_playlist(self):
        self.room1.add_song_to_playlist(self.song1)
        self.assertEqual("Sorry, not on our playlist", self.room1.favourite_song_on_playlist(self.guest2.fav_song, self.guest2))

        
        
        
        

