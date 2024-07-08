#a = cards in hands and feild
#b = monster lv
#x = xyz monster
#y = fusion monster = monster lv
a = 0
b = 0
a = int(input())
b = int(input())

#a = 2*x + y(=b)
#(a - b) /2 = x
#b = y

x = (a - b) / 2


# xyz to banish = x
print("xyz monster level :"+str(x))
 


# fusion to banish = y = b
print("fusion monster level :"+str(b))
print("if level"+str(b)+"futuon monster is banished by pot, can use cannon now.)
