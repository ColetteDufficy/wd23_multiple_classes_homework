class Room:
    
    def __init__(self, room_name, max_capacity, till):
        self.room_name = room_name
        self.max_capacity = max_capacity
        self.till = till
        self.number_of_guests = []
        self.playlist = []
        
        
    def guest_count(self):
        return len(self.number_of_guests)
        
    def check_in(self, guest):
        self.number_of_guests.append(guest)

    def check_out(self, guest):
        self.number_of_guests.remove(guest)
            
    def add_song_to_playlist(self, song):
        self.playlist.append(song)
        
    def check_room_capacity(self, guest):
        if len(self.number_of_guests) < self.max_capacity:
            self.check_in(guest)
            return self.guest_count()
    
    
        # else:
        #     return f"Sorry, the {self.room_name} is full"
        
              
        
        # if the len of number of guests less than max cpaity interger, then the room is not full
        # add guest
        # else
        # return a string - sorry room is full
        # breakpoint()
        
        
        
        
        # is the len of number of guests == max cpaity interger, - true or false
        # if true, no more guests
        # if false, add a guest