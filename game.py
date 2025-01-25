# Rock, Paper and Scissors game
import random

#declaring global variables
playing = "y"
player_choice = 'n'
comp_choice = "none"
games_won = 0
games_lost = 0
games_played = 0

my_list = ["r", "p", "s"]    #list of possible choices

#defining functions

# random selection of r, p or s from the mylist and replacing result with a full word
def comp_selection( mylist):
    global comp_choice

    comp_choice = mylist[random.randint(0, 2)] #random selection of r, s or p
    if comp_choice == "r":
        comp_choice = "Rock"
    elif comp_choice == "s":
        comp_choice = "Scissors"
    else:
        comp_choice = "Paper"
    return comp_choice

#getting user choice
def user_selection(my_list):
    global player_choice
    player_choice = str(input("Enter a choice: Rock(r), Paper(p), Scissors(s):"))
    while player_choice not in my_list:                                             #checking if user typed  r, p or s
        player_choice = str(input("Incorrect character. Please enter your choice: r for Rock, p for Paper or s for Scissors:"))
    #if correct character selected then overwrite with the word
    if player_choice == "r":
        player_choice = "Rock"
    elif player_choice == "s":
        player_choice = "Scissors"
    else:
        player_choice = "Paper"
    return player_choice

#comparing choices
def check_winner(player_choice, comp_choice):

    global games_won
    global games_lost
    global games_played

    games_played += 1           #increase no of games played
    if player_choice == comp_choice:            #same selection
        print ("It's a tie")
    # user winning possibilities and increasing winnings counter
    elif (player_choice == "Rock" and comp_choice == "Scissors") or ( player_choice == "Paper" and comp_choice == "Rock") or (player_choice == "Scissors" and comp_choice == "Paper"):
        games_won +=1
        print ("Congratulations, You won")
    else:                       #otherwise user lost & counter increase
        games_lost +=1
        print ("I'm sorry but you lost")

#START - Rules
print(" ")
print("Welcome to the game of Rock, Paper, Scissors")
print("The Winning Rules are as follows:")
print("Rock smashes Scissors.")
print("Paper covers Rock.")
print("Scissors cut Paper.")
print(" ")

#game
while playing != "n":                                                       #looping the game
    user_selection(my_list)                                                 # calling the function for player choice
    print("Computer selection is: " +comp_selection(my_list))               # calling the function and printing comp choice
    print("You have selected: ", player_choice + ", and computer: ", comp_choice)   # printing both choices
    check_winner(player_choice, comp_choice)                                        # comparing choices
    print(" ")
#overwrite variable 'playing' by user
    playing = str(input("Play again? Press 'n' to exit or any other key to continue"))
# if 'n'' typed game stopped and printing final results
print("   Final Scores:")
print("Played: %d time(s)" % games_played)
print("Player won: %d time(s)" % games_won)
print("Computer won: %d time(s)" % games_lost)
print("Draw: %d time(s)" % (games_played-games_won-games_lost))
print("         BYE")
