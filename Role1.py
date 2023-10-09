#In this program we are defining the first role as a "DRAGON" and we display its attributes.
#The attributes consists of "Intelligence", "Strength", "Dexterity" and, "Health".
#Each attribute ranges from a scale -2 - 2.
#The -2 being very bad, -1 being bad, 0 being neutral, 1 being good and 2 being very good.
#The user must enter number "1" to become that role which will then list the roles stats.


Role1 = "1"

Intelligence = -2
Strength = 2
Dexterity = 0
Health = 2

General_Combination = Intelligence + Strength + Dexterity + Health

print("                          *DRAGON ROLE*                            ")
selected_role = input("Select your role as a dragon and hit 1 to register that role: ")
if selected_role == Role1:
        Intelligence = -2
        Strength = 2
        Dexterity = 0
        Health = 2
        print ("*You have selected to be a dragon as your role and his attributes are as follows:*")
        print ("Intelligence =", Intelligence)
        print ("Strength =", Strength)
        print ("Dexterity =", Dexterity)
        print ("Health =", Health)


