import numpy as np
#Q1
a=np.array([1,2,3,4,5])
add=a+2
print(add)
mul=a*3
print(mul)
div=a/2
print(div)

#Q2
rev=a[::-1]
print("Reversed array is ",rev)
x = np.array([1,2,3,4,5,1,2,1,1,1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
modex=np.bincount(x).argmax()
print("Mode of array x ",x,"is",modex)
modey=np.bincount(y).argmax()
print("Mode of array x ",y,"is",modey)

#Q3
my = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(my[0,1],my[2,0])

#Q4
Prabh=np.linspace(10,100,25)
print(Prabh)
print("Shape of Prabh is ",Prabh.shape,"Dimensions are ",Prabh.ndim,"Data type is",Prabh.dtype)
print(Prabh.reshape(25,1))
print(Prabh.T)

#Q5
ucs420_Prabh=np.array([[ 10, 20, 30,],[ 40, 50, 60],[70, 80, 90],[15, 20, 35]])
print("Mean :",np.mean(ucs420_Prabh),"Median :",np.median(ucs420_Prabh),"Max :",np.max(ucs420_Prabh),"Min :",np.min(ucs420_Prabh))
reshaped_ucs420_Prabh=ucs420_Prabh.reshape(4,3)
print(reshaped_ucs420_Prabh)
resized_ucs420_Prabh=np.resize(ucs420_Prabh,(2,3))
print(resized_ucs420_Prabh)
