#In this program we are defining the first role as a "P.E.K.K.A" and we display its attributes.
#The attributes consists of "Intelligence", "Strength", "Dexterity" and, "Health".
#Each attribute ranges from a scale -2 - 2.
#The -2 being very bad, -1 being bad, 0 being neutral, 1 being good and 2 being very good.
#The user must enter number "2" to become that role which will then list the roles stats.


Role1 = "2"

Intelligence = 1
Strength = 2
Dexterity = 2
Health = -1

General_Combination = Intelligence + Strength + Dexterity + Health

print("                          *P.E.K.K.A ROLE*                            ")
selected_role = input("Select your role as a P.E.K.K.A and hit 2 to register that role: ")
if selected_role == Role1:
        Intelligence = 1
        Strength = 2
        Dexterity = 2
        Health = -1
        print ("*You have selected to be a P.E.K.K.A as your role and his attributes are as follows:*")
        print ("Intelligence =", Intelligence)
        print ("Strength =", Strength)
        print ("Dexterity =", Dexterity)
        print ("Health =", Health)

