#Q6.1
a="Prabhsimrat"
c=0
vowels="aeiouAEIOU"
for x in a:
    if x in vowels:
        c=c+1
print(c)

#Q6.2
rev=a[::-1]
print(rev)

#Q6.3
for x in a:
    if x not in rev:
        print("not plaindrome")
