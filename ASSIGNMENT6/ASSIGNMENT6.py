import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
m=float(input("Enter value to use in function: "))
x=np.linspace(-10, 10, 50)
y=m-x**2
y1=m-np.sin(x)
plt.plot(x, y, label='y = m - x^2', color='y', marker="o")
plt.plot(x, y1, label='y = m - sin(x)', color='b', marker="s")
plt.title("Comparison of y = m - x^2 and y = m - sin(x)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.grid(True)
plt.show()


#Q2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
mydata = {
    "Subject": ["Math", "Science", "English", "History", "Computer Science"],
    "Score": [85, 90, 38, 28, 95]
}
df = pd.DataFrame(mydata)
g=sns.barplot(x="Subject", y="Score", data=df)
plt.title("Scores in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.grid(axis="y")
plt.show()

#Q3
import numpy as np
import matplotlib.pyplot as plt


roll_number = 102317135 
np.random.seed(roll_number)
data = np.random.randn(50)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(np.cumsum(data), marker="o", linestyle="-", color="b")
axes[0, 0].set_title("Cumulative Sum Line Plot")
axes[0, 0].set_xlabel("Index")
axes[0, 0].set_ylabel("Cumulative Sum")
axes[0, 0].grid(True)
noise = np.random.randn(50) * 0.5
axes[0, 1].scatter(range(50), data + noise, color="r", marker="x")
axes[0, 1].set_title("Scatter Plot with Noise")
axes[0, 1].set_xlabel("Index")
axes[0, 1].set_ylabel("Value")
axes[0, 1].grid(True)
plt.show()

#Q4
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('https://github.com/AnjulaMehto/MCA/raw/main/company_sales_data.csv')

sns.lineplot(x='month_number', y='total_profit', data=df, marker='o', color='b')
plt.title('Total Profit per Month')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.grid(True)
plt.show()

product_columns = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
for product in product_columns:
    sns.lineplot(x='month_number', y=product, data=df, marker='o', label=product)
plt.title('Product Sales per Month')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.legend(title='Products')
plt.grid(True)
plt.show()


attributes = df.columns[1:-1]
num_attributes = len(attributes)
fig, axes = plt.subplots(nrows=num_attributes, ncols=1, figsize=(12, 4 * num_attributes))
for i, attribute in enumerate(attributes):
    sns.barplot(x='month_number', y=attribute, data=df, ax=axes[i])
    axes[i].set_title(f'{attribute.capitalize()} Sales per Month')
    axes[i].set_xlabel('Month Number')
    axes[i].set_ylabel(f'{attribute.capitalize()} Sales')
    axes[i].grid(True)
plt.tight_layout()
plt.show()

