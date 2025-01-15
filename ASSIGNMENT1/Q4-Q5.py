#Q4.1
for x in range(1,11):
    print(x)
print("First loop done")

#Q4.2
i=1;
while i<=10:
    print(i)
    i=i+1
print("Second loop done")

#Q4.3
sum=0
for x in range(1,101):
    sum=sum+x
print(sum)

#Q5.1
L=[23,11,6,70,2]
print("Max and min values are ",max(L),min(L))

#Q5.2
CG={
"Maths":"A",
"Electronics":"A-",
"C":"A"
}

#Q5.3
L.sort()
print("List in ascending order ",L)
L.sort(reverse=True)
print("List in descending order ",L)

#5.4
CG2={
    "ED":"A-",
    "Manpro":"A",
    "Maths":"A",
    "Physics":"A"
}
CG.update(CG2)
print("\nOverall CG is ",CG)
print("CG in Maths is ",CG["Maths"])

