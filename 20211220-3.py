import random
number = random.randint(1,6)
szam = int(input("Adj megy egy számot: "))
if(number > szam):
    print("A számod kisebb mint a gép száma")
elif(number < szam):
    print("A számod nagyobb mint a gép száma")
else:
    ("Ugyan akkora")