class Room:
    
    def __init__(self, room_name, max_capacity, till):
        self.room_name = room_name
        self.max_capacity = max_capacity
        self.till = till
        self.number_of_guests = []
        playlist = []
        
        
    def guest_count(self):
        return len(self.number_of_guests)
        
    def check_in(self, guest):
        self.number_of_guests.append(guest)

    def check_out(self, guest):
        self.number_of_guests.remove(guest)
            
            