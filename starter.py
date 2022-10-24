# Import Libraries
import os
import glob
import time


#Globals
# Initialize the GPIO Pins
os.system('modprobe w1-gpio')  # Turns on the GPIO module
os.system('modprobe w1-therm') # Turns on the Temperature module

# Finds the correct device file that holds the temperature data
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# A function that reads the sensors data and returns it as a string
def read_temp_raw():
    f = open(device_file, 'r') # Opens the temperature device file
    lines = f.readlines() # Returns the text containing the readings
    f.close()
    return lines

# Convert the value of the sensor into a temperature
def read_temp():
    ##TODO read the current temperature, make sure the first string contains 'YES'

    ##TODO Get the position of the = sign in the second string

    ##TODO Convert the string to the right of the equal sign to an int

    ##TODO Divide that number by 1000 to get the celsius value

    ##TODO Convert C to F and return the two values as a tuple

    #replace this with your return
    pass

def main():
    cel, far = read_temp()


#boiler plate python code that runs the main funciton
if __name__ == '__main__':
    main()