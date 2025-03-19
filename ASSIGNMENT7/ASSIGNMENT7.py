import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(102317135)#Roll number seed
sales=np.random.randint(1000,5000,size=(12,4))#Range from 1000 to 5000 with size 12x4
months= ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
df=pd.DataFrame(sales,columns=[ "Electronics", "Clothing", "Home", "Sports" ],index=months)#Creaated dataframe with data from sales,columns having names as mentioned and having index as months 
print(df)
print("\nFirst 5 rows are ",df.head())
print("\nSum for each Category is ",df.sum())
print("\nSum for each Month is ",df.sum(axis=1))
df["totalsales"]=df.sum(axis=1)
df["growth"]=df["totalsales"].pct_change()*100#%age change function to calculate change between each index
#print(df)

for i in range(len(df)):
    if i%2== 0:  # Check if index (month) is even
        df.iloc[i,df.columns.get_loc("Electronics")] *= 0.9  # Apply 10% discount to Electronics
    else:
        df.iloc[i,df.columns.get_loc("Clothing")] *= 0.85  # Apply 15% discount to Clothing
# Display the updated DataFrame
print(df)




# plot monthly sales trends for each category using line plots
for category in ["Electronics", "Clothing", "Home", "Sports"]:
    plt.plot(df.index,df[category],marker='o',label=category)

plt.title("Monthly Sales Trends for Each Category")
plt.xlabel("Month")
plt.ylabel("Sales (Units)")
plt.show()

#create box plots to show the sales distribution for each category
sns.boxplot(data=df[["Electronics", "Clothing", "Home", "Sports"]])
plt.title("Sales Distribution for Each Category")
plt.ylabel("Sales (Units)")
plt.show()



arr=np.array([[1, -2, 3],[-4, 5, -6]])
print(abs(arr))
fl=arr.flatten()
print(fl)
print("For Flatened array \nMean:",np.mean(fl),"Median",np.median(fl),"Mode",np.bincount(fl).argmax())
print("For each row of arr:\nMean:",np.mean(arr,axis=0),"Median",np.median(arr,axis=0),"Mode",np.bincount(arr,axis=0).argmax())
print("For each column of arr:\nMean:",np.mean(arr,axis=1),"Median",np.median(arr,axis=1),"Mode",np.bincount(arr,axis=1).argmax())
a=np.array([-1.8,-1.6,-0.5,0.5,1.6,1.8,3.0])
print("\nFloor for array a",np.floor(a),"Ceiling :",np.ceil(a),"Truncated :",np.trunc(a),"Rounded :",np.round(a))

#Q4
def swap(a,i1,i2):
  temp=a[i1]
  a[i1]=a[i2]
  a[i2]=temp
  return a
my=[10,20,30,40,50]
print(my)
print(swap(my,2,3))
