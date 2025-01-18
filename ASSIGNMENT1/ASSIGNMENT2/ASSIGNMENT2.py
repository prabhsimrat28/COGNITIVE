#ASSIGNMENT 2
import random
#Q1
L=[10,20,30,40,50,60,70,80]
L.append(200)
L.append(300)
print(L)
L.remove(10)
L.remove(30)
print("\nList after removing 10 and 30",L)
L.sort()
print("List after sorting ",L)
L.sort(reverse=True)
print("List sorted in reverse ",L)

#Q2
scores= (45, 89.5, 76, 45.4, 89, 92, 58, 45)
print("Max and min in tuple are ",max(scores),min(scores))
print("Index of Highest score is ",scores.index(max(scores)))
print("Frequency of lowest score is ",scores.count(min(scores)))
if 76 in scores:
    print("76 is present")
else:
    print("76 not present")

#Q3
Random=[]
i=100
oc=0
ec=0
prc=0
while i>0:
    Random.append(random.randint(100,900))
    i=i-1
print(Random)
for x in Random:
    if x%2==0:
        ec=ec+1
    else:
        oc=oc+1
        for i in range(2,x):
            if x%i==0:
                prc=prc+1
print("Odd count",oc,"Even Count",ec,"Prime count",prc)

#Q4
A={34, 56, 78, 90}
B = {78, 45, 90, 23}
print("A union B",A.union(B))
print("A intersection B",A.intersection(B))
print("A - B",A.symmetric_difference(B))
print("is A subset of B",A.issubset(B),"is B superset of A",B.issuperset(A))
sc=int(input("Enter score to remove"))
for x in A:
    if x==sc:
        A.remove(x)
        print("removed x")

#Q5
data = {"city": "New York", "population": 8419600, "area": 468.9}
print(data)
data["loaction"]=data.pop("city")
print(data)