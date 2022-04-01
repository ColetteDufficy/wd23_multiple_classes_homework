class Room:
    
    def __init__(self, room_name, max_capacity, till):
        self.room_name = room_name
        self.max_capacity = max_capacity
        self.till = till
        self.list_of_guests = []
        self.playlist = []
        
    
    def head_count(self):
        return len(self.list_of_guests)
        
    def check_in(self, guest):
        self.list_of_guests.append(guest)
        self.max_capacity -= 1

    def check_out(self, guest):
        self.list_of_guests.remove(guest)
        self.max_capacity += 1

    def add_song_to_playlist(self, song):
        self.playlist.append(song)
        
    def room_has_capacity(self, guest):
        if len(self.list_of_guests) < self.max_capacity:
            self.list_of_guests.append(guest)
            return f"Welcome to {self.room_name}!"
        else:
            return f"Sorry, the {self.room_name} is full"
        
              
     
        