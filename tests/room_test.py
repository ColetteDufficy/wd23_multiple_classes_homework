import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Red Room", 7)
        self.room2 = Room("Green Room", 3)
        
        self.guest1 = Guest("Winkie", 50, "Wannabe")
        self.guest2 = Guest("Leigh", 40, "Business Time")
        self.guest3 = Guest("Becky", 20, "Let it Go")
        
        self.song1 = Song("Spice Girls", "Wannabe")
        self.song2 = Song("Mr Brightside", "The Killers")
        
        
        
        

