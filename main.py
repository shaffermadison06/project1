#Thsi will be an interactive game on hang-man. The computer will come up with the word and thge user will only have a certain amount of guesses to figure out what the word is before they lose

#Introuduce the player to the game
def introduce():
  print ("Welcome to the game of Hangman")

choice = ("yes")
option = str(input("Do you want to play this game? "))
for choice in option:
  if (choice != str("yes")):
    break

#set the wrod for hang-man
word = "computer science"

#decide how many turns the player gets
turns = 20

#create the guess variable, but leave it blank to use later
guesses = ''

#wreate a while loop that checks how many turns the user has done and what should happen after the user guesses
while turns > 0:         

    #make a counter for the guesses that are wrong
    failed = 0             

    #make a for loop for the characters in computer science 
    for character in word:      
       #make an if statment to see if the users guess is correct or not
      if character in guesses:  
        #print for user
        print (character)  
      else:
        #if the users guess is incorecct it will keep the dash
            print ("_"),     
       
        #the users turn will then be counted as a fail
            failed += 1    

    #if the user guesses the word before their turns are up then the user won. print for the user
    if failed == 0:        
      print ("You won")

    #ask user to guess the character
    guess = str(input("guess a character:"))

    #set the players guess to the variable guesses that was created at the begining
    guesses += guess            
 #if the guess is not found in the hang-man word the user gets 1 less turn. print for user
if guess not in word:  
  turns -= 1      
  print ("Wrong. You have %i my guesses"%(turns))  

 
    # if the turns are equal to zero print you lose
if turns == 0:           
  print "You Lose"
    #if the user is out of turns, lets them know they lost
    if turns == 0:           
      print ("You Lost")
