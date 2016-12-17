# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

chances = 7
secret_number = 0
number_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here  
    global chances
    global secret_number
     
    if number_range == 100:
        secret_number = random.randrange(0,100)
        chances = 7
        
    elif number_range == 1000:
        secret_number = random.randrange(0,1000)
        chances = 10
        
    print "New game. Range is 0 to "+str(number_range)
    print "Number of remaining guesses is "+ str(chances)    
    print ""
        
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number_range
    number_range = 100
    
    new_game()
    
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number_range
    number_range = 1000
    
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global chances
    
    print "Your guess was " + guess
    
    chances -=1
    
    print "Number of remaining guesses is " + str(chances)
    
    #logic for checking the guess against secret_number
    if int(guess) == secret_number:
        print "Correct, You won!"
        print ""
        new_game()
        
    elif chances==0:
        print "You ran out of guesses. The number was: "+str(secret_number)
        print ""
        new_game()
    
    elif int(guess) > secret_number:
        print "Lower!"
    
    elif int(guess) < secret_number:
        print "Higher!"
      
    print ""
    

# create frame
frame = simplegui.create_frame("Guess The Number", 400, 400)

# register event handlers for control elements and start frame
frame.add_button("Range from 0 to 100", range100, 100)
frame.add_button("Range from 0 to 1000", range1000, 100)
frame.add_input("Input your guess", input_guess, 100)

frame.start()

# call new_game 
new_game()
