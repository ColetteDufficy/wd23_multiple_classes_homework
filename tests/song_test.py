import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Spice Girls", "Wannabe")
        self.song2 = Song("Mr Brightside", "The Killers")