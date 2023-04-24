import random


for i in range(20):
    a = random.randint(1, 2000)
    b = random.randint(1, 99)
    amount = str(a) + '.' + str(b)
    print("('440881200011230419', '" + amount + "', '交学费', NOW())")