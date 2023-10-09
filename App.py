#The program imports various other files to combine other pieces of code to fully function such as different roles and etc.

import random

#The variable "roles" is defined here that has 2 roles "DRAGON" and "P.E.K.K.A" in it with their respected attributes as shwon.

roles = {
    "DRAGON": {"Strength(ST)": 2, 
               "Dexterity(DX)": 0, 
               "Intelligence(IQ)": -2, 
               "Health (HT)": 2},

    "P.E.K.K.A": {"Strength(ST)": 2, 
                  "Dexterity(DX)": 2, 
                  "Intelligence(IQ)": 1, 
                  "Health (HT)": -1},
}

#The variable "Missions" is defined here that has 3 missions that are associated with the role and thier attributes and have some objective to achieve.

Missions = [
    {"n1": 
     "The Fortune Hunt", "attribute": "Strength(ST)", "description": 
     "First you have to acquire gold and elixir as treasure."},
    {"n1": 
     "The Barbarian King Encounter", "attribute": "Dexterity(DX)", "description": 
     "Now you face the undisputed Barbarian King."},
    {"n1": 
     "Knowledge Test", "attribute": "Intelligence(IQ)", "description": 
     "Lastly you now have to answer some facts."},

]

#Here the 2 print statements start the program by welcoming the user to the game followed up by a motto

print("                                        |Welcome to Clash of Warriors game|")
print ("                                   *Where Greantess and Strategy Has No Limit*")
print("*You will face 3 levels as a DRAGON or P.E.K.K.A where you must roll more than 8 for each level to win the game.* ")

#Here the prompt of choosing a role comes up that shows the 2 roles in upper case. 

print("Choose your role:")
for cow, role in enumerate(roles.keys(), start=1):
    print(f"{cow}. {role.upper()}")

#While statment is made as it defines the variable "option" which asks the user for an input of either 1 for DRAGON or 2 for P.E.K.K.A.
#If statement is made for the "option" variable that takes in the value of 1 or 2 and breaks at the end.
#The prompt "Invalid choice, please enter 1 or 2" comes up if the user enters the wrong number.

while True:
        option = int(input("Enter 1 for DRAGON or 2 for P.E.K.K.A: "))
        if option in [1, 2]:
            s_r = list(roles.keys())[option - 1]
            break
        else:
            print("Invalid choice, please enter 1 or 2.")

#The program prints out if you are either a DRAGON or P.E.K.K.A in upper case after inputting 1 or 2 for the roles.

print(f"You are now a {s_r.upper()}!")

#Here we define 2 6-sided dice and when it rolls the values can range from 2-12.
#The program defines "outcome" with three variables in them (role, challenge and dice).
#If statements followed by elif statements makes the condition for each roll and what its output will be depending on the value we get after rolling the dice.


def two_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def outcome(role, challenge, dice):
    Behaviour = roles[role][challenge["attribute"]]
    if dice <= 3 and dice >= 2:
        print(f"Critical Loss: {challenge['n1']} challenge is lost and the {challenge['attribute']} attribute that it's based on has decreased.")
        roles[role][challenge["attribute"]] -= 1
    elif dice <= 7 and dice >= 4:
        print(f"Loss: {challenge['n1']} challenge is lost , no changes in your attributes.")
    elif dice <= 10 and dice >= 8:
        print(f"Win: {challenge['n1']} challenge is won, no change in the character's attributes.")
    elif dice <=12 and dice >= 11:
        print(f"Critical Win: {challenge['n1']} challenge is won and the  {challenge['attribute']} attribute that it's based on increases.")
        roles[role][challenge["attribute"]] += 1
    else:
        I = "The input you have entered is invalid."
        print(I)
        
#For loops is made for "challenge" in "Misisons" and a new line is created with the code "\n" that takes the challenge and the "Missions" as "n1".
#It takes the challenge and puts the description with it and takes the input from the user when the user hits enter on the keyboard.
#The "roll_result" is defined as the "two_dice" and outputs the randomly generated roll result.

for challenge in Missions:
    print(f"\nChallenge: {challenge['n1']}")
    print(challenge["description"])

    input("Hit Enter on the keyboard for the dice to roll:")

    roll_result = two_dice()
    print(f"You rolled a {roll_result}.")

    outcome(s_r, challenge, roll_result)

#The if statement here takes the value if its greater than or equal too 0 for the values in the roles variable and prints if you won or lost.
#It also tells the user they have finished the game in a seperate line and prints out the win or loss result with your selected role in upper case.

print("\nYou have completed the game!")
if all(value >= 0 for value in roles[s_r].values()):
    print(f"WOW YOU HAVE DONE IT SOLDIER! YOU DEFENDED YOUR LAND AND YOU ARE NOW HAILED AS THE NEW KING! {s_r.upper()}!")
else:
    print(f"Sadly you were unsuccessful, you couldn't complete the quest as a {s_r.upper()}. Dont worry we'll get em next time!")





