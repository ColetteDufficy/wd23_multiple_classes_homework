
class Guest:
    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet  
        self.fav_song = fav_song
        
    def sufficient_funds(self, room):
        return self.wallet >= room.entry_fee
    
    def pay_entry_fee(self, room):
        if self.sufficient_funds(room):
            self.wallet -= room.entry_fee
            return self.wallet
        else:
            return "Sorry, you dont have enough money"
        