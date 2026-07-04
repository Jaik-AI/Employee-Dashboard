import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('employees.csv')
print("="*34)
print("\tEmployees Report")
print("="*34)
print("\n=== Highest Paid Employee ===\n")
high_sal = df['Salary'].idxmax()
print(f"Name   : {df.loc[high_sal,'Name']}\nSalary : ₹{df.loc[high_sal,'Salary']:,}\n")

print("\n=== Lowest Paid Employee ===\n")
low_sal = df['Salary'].idxmin()
print(f"Name   : {df.loc[low_sal,'Name']}\nSalary : ₹{df.loc[low_sal,'Salary']:,}\n")

print("\n=== Average Salary By Department ===\n")
avg_sal_dep = df.groupby("Department")["Salary"].mean()
for dep,sal in avg_sal_dep.items():
    print(f"{dep:<9} : ₹{sal:,.2f}")

print("\n=== Employees In Each Department ===\n")
emp_dept = df['Department'].value_counts()
for dep,cnt in emp_dept.items():
    print(f"{dep:<9} : {cnt} Employees")

print("\n=== Highest Salary ===")
print(f"₹{df['Salary'].max():,}")

print("\n=== Lowest Salary ===")
print(f"₹{df['Salary'].min():,}")

print("\n=== Average Age ===")
print(f"{df['Age'].mean():.2f} Years")

print("\n=== Most Experienced Employee ===\n")
most_exp = df['Experience'].idxmax()
print(f"Name       : {df.loc[most_exp,"Name"]}\nExperience : {df.loc[most_exp,"Experience"]} Years")

print("\n=== Youngest Employee ===\n")
yng_emp = df["Age"].idxmin()
print(f"Name : {df.loc[yng_emp,"Name"]}\nAge  : {df.loc[yng_emp,"Age"]} Years")

print("\n=== Oldest Employee ===\n")
old_emp = df["Age"].idxmax()
print(f"Name : {df.loc[old_emp,"Name"]}\nAge  : {df.loc[old_emp,"Age"]} Years")

print("\n===  Employee Above Average Salary ===\n")
avg_sal = df["Salary"].mean()
abv_avg_sal = df[df["Salary"]>avg_sal].index
print("Name\t Department\tSalary\t   Experience")
print("-"*45)
for i in abv_avg_sal:
    print(f"{df.loc[i,'Name']}\t {df.loc[i,'Department']:<8}\t₹{df.loc[i,'Salary']:,}\t   {df.loc[i,'Experience']} Years")

print("\n===  Employees with More Than 5 Years Experience ===\n")
more_5_exp = df[df["Experience"]>5].index
print("Name\t Department\tSalary\t   Experience")
print("-"*45)
for i in more_5_exp:
    print(f"{df.loc[i,'Name']}\t {df.loc[i,'Department']:<8}\t₹{df.loc[i,'Salary']:,}\t   {df.loc[i,'Experience']} Years")

print("\n===  Top 3 Highest Paid Employees ===\n")
top_3 = df.sort_values("Salary",ascending=False).head(3)
for i,(_,row) in enumerate(top_3.iterrows(),start=1):
    print(f"{i}. Name       : {row['Name']}\n   Salary     : ₹{row['Salary']:,}\n   Department : {row["Department"]}\n")

print("\n===  Department with Highest Average Salary ===\n")
print(f"Department : {avg_sal_dep.idxmax()}")

# Bar Chart
avg_sal_dep = df.groupby("Department")['Salary'].mean()
dep = avg_sal_dep.index
sal = avg_sal_dep.values
plt.figure(figsize=(15,10))
plt.subplot(3,2,1)
plt.bar(dep,sal)
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Salary')

#Pie Chart
plt.subplot(3,2,2)
emp_dep = df['Department'].value_counts()
dep1 = emp_dep.index
emp_cnt = emp_dep.values
plt.pie(emp_cnt,labels=dep1,autopct='%1.1f%%',startangle=90)
plt.title('Employees In Each Department')

#Scatter Chart
plt.subplot(3,2,3)
plt.scatter(df['Experience'],df['Salary'],alpha=.8)
plt.title("Experience vs Salary")
plt.xlabel('Experience')
plt.ylabel('Salary')

#Histogram
plt.subplot(3,2,4)
plt.hist(df['Salary'],bins=6)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('No. of employees')
plt.grid(axis='y')

plt.subplot(3,2,5)
avg_sal_dep1 = df.groupby('Department')['Salary'].sum()
plt.bar(avg_sal_dep1.index,avg_sal_dep1.values)
plt.title("Department Salary Comparison")
plt.xlabel("Department")
plt.ylabel("Salary")

plt.subplot(3,2,6)
avg_exp_dep = df.groupby('Department')['Experience'].mean()
plt.bar(avg_exp_dep.index,avg_exp_dep.values)
plt.title('Average Experience by Department')
plt.xlabel('Department')
plt.ylabel('Experience')

plt.tight_layout()
plt.show()