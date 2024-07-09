#a = cards in hands and feild
#b = monster lv
#x = xyz monster
#y = fusion monster = monster lv



#a = 2*x + y(=b)
#x = (a - b) /2
#y = b 

a = input("Enter the number of cards in hand and field: ")
b = input("Enter the monster level: ")

try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Invalid input: Please enter valid integers for the number of cards and monster level.")
    exit()
  
#a = 2*x + y(=b)
#x = (a - b) /2
#y = b 

x = (a - b) / 2

# Check if x is an integer
if x.is_integer():
    x = int(x)  # Convert x to an integer
    print("xyz monster level: ", x)
    print("fusion monster level: ", b)
    print("if level {} fusion monster is banished by pot, you can use the cannon now.".format(b))
else:
    #print("Cannot banish the monsters: The calculated XYZ monster level is not an integer.")
    print("cant be used now")
    print("if pot has banished level " + str(b) + "fusion monster, banish as" + str(a) )
