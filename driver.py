# Driver class definition
class Driver:
    #constructor
    def __init__(self):
        self.name = ""
        self.miles = 0
        self.time = 0

    # Method to calculate speed from the attributes of a Driver object
    def get_speed(self):
         hours = float(self.time)/60
         if hours == 0:
             return hours
         return self.miles/hours
