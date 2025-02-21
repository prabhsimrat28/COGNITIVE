import numpy as np
import matplotlib.pyplot as plt
#Q1
gfg=np.array([[4,1,9],[12,3,1],[4,5,6]])
print("Sum is :",gfg.sum(),"Row sum is: ",gfg.sum(axis=1),"sum of Column is :",gfg.sum(axis=0))


#Q2
array = np.array([10, 52, 62, 16, 16, 54, 453])
print(np.sort(array))
print("\n",array.argsort())
print("First 4 smallest elements are: ",np.sort(array)[:4],"first 5 largest elements are: ",np.sort(array)[-5:])
arr=np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
for i in arr:
    if(i==int):
        print("integer",i)
    else:
        print("Float",i)

#Q3
f="Prabhsimrat"
l="Singh"
X=0
for c in f:
   X=X+ord(c) 
for c in l:
    X=X+ord(c)
print(X)
sales=np.array([X,X+50,X+100,X+150,X+200])
print(sales)
sales=sales+(((X%5)+5)/100)*sales
print("Sales after tax: ",sales)
for i in range(len(sales)):
    if(sales[i]<X+100):
        sales[i]=sales[i]-0.05*sales[i]
    else:
        sales[i]=sales[i]-0.1*sales[i]
print("Discounted sale is :",sales)
weeksale=np.array([sales,sales+0.02*sales,sales+0.04*sales])
print(weeksale)

#Q4
x=np.linspace(-10,10,100)

y=x**2
ysin=np.sin(x)
ye=np.exp(x)
ylog=np.log(np.abs(x)+1)

plt.plot(x, y,label='y = x^2', color='y',marker="y")
plt.plot(x, ysin,label='y = sin(x)', color='b',marker="o")
plt.plot(x, ye,label='y = exp(x)', color='r', marker="i")
plt.plot(x, ylog,label='y = log(|x|+1)', color='g', marker="m")

plt.title("y = x^2")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()