import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Winkie", 50, "Wannabe")
        self.guest2 = Guest("Leigh", 40, "Business Time")
        self.guest3 = Guest("Becky", 20, "Let it Go")
        
    
    def test_guest_has_name(self):
        self.assertEqual("Becky", self.guest3.name)
        
    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest1.wallet)
        
    def test_guest_has_fav_song(self):
        self.assertEqual("Business Time", self.guest2.fav_song)