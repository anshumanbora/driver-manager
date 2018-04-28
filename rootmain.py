# Example input:
# Driver Dan
# Driver Alex
# Driver Bob
# Trip Dan 07:15 07:45 17.3
# Trip Dan 06:12 06:32 21.8
# Trip Alex 12:01 13:16 42.0
# Expected output:
# Alex: 42 miles @ 34 mph
# Dan: 39 miles @ 47 mph
# Bob: 0 miles

import datetime
from driver import  Driver
import sys

# Method to calculate totoal time travelled by the driver
def calculate_time(time_1,time_2):

    # Converted the time to a datetime object just to make the code more elegant.
    # Alternatively I could have just converted the string type time into int and
    # calculated the desired time from it.

    new_time_2 = datetime.datetime.strptime(time_2,'%H:%M')
    new_time_1 = datetime.datetime.strptime(time_1,'%H:%M')
    hours = new_time_2.hour - new_time_1.hour
    if hours==0:
        minutes = new_time_2.minute-new_time_1.minute
    else:
        minutes = new_time_2.minute+(60-new_time_1.minute)+(hours-1)*60
    return minutes

# Method to create a new driver object
def create_object(entry,dictionary):

    new_driver = Driver()
    new_driver.name = entry[1]
    # Each entry in the dictionary is an object of type Driver and
    # can be accessed with the key which is the name of the driver
    dictionary[new_driver.name]=new_driver
    return dictionary

def fill_object(entry,dictionary):

    miles = float(entry[-1])
    name = entry[1]
    time = calculate_time(entry[2],entry[3])
    # adding time and miles for the drivers in their respective
    # objects in the dictionary
    dictionary[name].miles+=miles
    dictionary[name].time+=time
    return dictionary

def read_write(input_file,output_file,dictionary):

     try:
    # This line of code
        with open(input_file) as f:
            for line in f:
                entry = line.split()
                if entry[0]=="Driver":
                    dictionary = create_object(entry,dictionary)
                elif entry[0]=="Trip":
                    dictionary = fill_object(entry,dictionary)
                else:
                    print("Invalid Entry:",entry)
     except EnvironmentError as e:
         print('Unable to open file because of Error:',e)

     #Sorting the dictionary w.r.t miles covered by the drivers
     dic = sorted(dictionary.items(), key=lambda x: x[1].miles, reverse=True)

     try:
        #opening output file and writing content in it
        with open(output_file,'w') as of:
            for key in dic:
                write_string = str(key[1].name)+' : '+str(round(key[1].miles))+ ' miles'
                # Invoking the class method to calculate speed of the current driver
                speed = key[1].get_speed()
                # Aviding rounding off speed if the value is less than 0.5 mph as it would give a speed = 0
                if speed>0 and speed<0.5:
                    # Limiting the precision to two digits after the decimal point
                    write_string+=' @ '+str(key[1].get_speed())[:4]+' mph'
                elif speed>=0.5:
                    write_string += ' @ ' + str(round(key[1].get_speed())) + ' mph'

                #writing to output file
                of.write(write_string+'\n')


     except EnvironmentError as e:
         print('Unable to open file because of Error:', e)




if __name__=="__main__":
    dictionary = {}
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    read_write(input_file,output_file,dictionary)
