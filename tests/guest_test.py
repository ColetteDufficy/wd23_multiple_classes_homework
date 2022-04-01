import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Winkie", 50, "Wannabe")
        self.guest2 = Guest("Leigh", 40, "Business Time")
        self.guest3 = Guest("Becky", 20, "Let it Go")
        self.guest4 = Guest("Erica", 5, "Maneater")
        
        self.room1 = Room("Blue Room", 7, 100, 12.99)
        
    
    def test_guest_has_name(self):
        self.assertEqual("Becky", self.guest3.name)
        
    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest1.wallet)
        
    def test_guest_has_fav_song(self):
        self.assertEqual("Business Time", self.guest2.fav_song)
        
    def test_sufficient_funds__true_if_enough(self):
        self.assertEqual(True, self.guest1.sufficient_funds(self.room1))

    def test_sufficient_funds__false_if_not_enough(self):
        self.assertEqual(False, self.guest4.sufficient_funds(self.room1))
        
    def test_wallet_balance_after_entry_fee__enough_money(self):
        self.assertEqual(37.01, self.guest1.pay_entry_fee(self.room1))

    def test_wallet_balance_after_entry_fee__not_enough_money(self):
        self.assertEqual("Sorry, you dont have enough money", self.guest4.pay_entry_fee(self.room1))
        

