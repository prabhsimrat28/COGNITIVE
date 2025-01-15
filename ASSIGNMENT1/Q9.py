#Q9.1
import random
i=5
while i>0:
    print(random.randint(0,100))
    i=i-1

#Q9.2
a=int(random.randint(0,99))
for x in range(2,a):
    if a%x==0:
        print("not prime")

#Q9.3
die=random.randint(1,6)
print("Dice number is ",die)

#Q9.4
L=[1,2,3,4,5,6,7]
random.shuffle(L)
print("Shuffeled list is ",L)

#Q9.5
a=random.choice(L)
print("randomly selected number is ",a)

#Q9.6
pas=[]
l=int(input("Enter length of password"))
while l>0:
    pas.append(int(random.randint(0,9)))
    l=l-1
print("Passoword is ",pas)

#Q9.7
r=random.randint(1,52)
print("randomly picked card is ",r)



