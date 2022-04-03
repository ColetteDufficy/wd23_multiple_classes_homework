class Room:
    
    def __init__(self, room_name, max_capacity, till, entry_fee):
        self.room_name = room_name
        self.max_capacity = max_capacity
        self.till = till
        self.list_of_guests = []
        self.playlist = []
        self.entry_fee = entry_fee
        
    
    def head_count(self):
        return len(self.list_of_guests)
        
    def check_in(self, guest):
        self.list_of_guests.append(guest)
        self.max_capacity -= 1

    def check_out(self, guest):
        self.list_of_guests.remove(guest)
        self.max_capacity += 1
        
    def room_has_capacity(self, guest):
        if len(self.list_of_guests) < self.max_capacity:
            self.list_of_guests.append(guest)
            return f"Welcome to {self.room_name}!"
        else:
            return f"Sorry, the {self.room_name} is full"

    def add_song_to_playlist(self, song):
        self.playlist.append(song)
        
        
    def charge_entry_fee(self, guest):
        if guest.sufficient_funds(self):
            guest.wallet -= self.entry_fee
            self.till += self.entry_fee
            return self.till
        
        
    def favourite_song_on_playlist(self, song, guest):
        for song in self.playlist:
            if guest.fav_song == song.title:
                return "Whoo hoo!"
        else:
            return "Sorry, not on our playlist"
              
     
        