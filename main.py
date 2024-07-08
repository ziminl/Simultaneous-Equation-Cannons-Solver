#a = cards in hands and feild
#b = monster lv
#x = xyz monster
#y = fusion monster = monster lv

a = input()
b = input()

#a = 2*x + y(=b)
#(a - b) /2 = x
#b = y

x = (a - b) / 2


# xyz to banish = x
print("xyz monster level :"+x)
 


# fusion to banish = y = b
print("fusion monster level :"+b)
print("if level"+b+"futuon monster is banished by pot, can use cannon now.)
