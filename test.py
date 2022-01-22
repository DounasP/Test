import random
binaryvalues=[]
values=[]

for i in range(3):  # αναθέτουμε random bool τιμές
    binaryvalues.append(bool(1))
print(binaryvalues)



for i in range(3):
    values.append(bool(random.getrandbits(1)))
print(values)
print("binaryvalues",binaryvalues)

