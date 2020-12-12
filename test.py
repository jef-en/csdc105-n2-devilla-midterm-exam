# Author          : Jefen B. De Villa
# Course and Year : BS Information Technology 2nd Year
# Filename        : test.py
# Description     : driver program 
# Honor Code      : I have received help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

from emmet import Emmet          # from file emmet import module Emmet

while True:                      # a while loop that will loop indefinitely
    tags = input()               # takes in the input of the user
    if tags.lower() == 'quit':   # if statement that will be satisfied if the conditions are met
        break                    # break statement that will terminate the loop
    else:                        
        e = Emmet(tags)          # create a new instance of class Emmet 
        print(e)                 # print statement that will print object e


    