#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

# Load employee dataset
df = pd.read_csv("../data/employees.csv")

# Display first 5 rows
print("Employee Dataset")
display(df.head())

# Check dataset information
print("Dataset Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())


# In[5]:


# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Salary with median
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Check missing values again
print("Missing Values After Cleaning:")
print(df.isnull().sum())

# Display cleaned data
display(df)


# In[6]:


# Calculate average salary by department

department_salary = df.groupby("Department")["Salary"].mean()

print("Average Salary by Department:")
print(department_salary)


# In[13]:


plt.figure(figsize=(8,5))

department_salary.plot(kind="bar", label="Average Salary"),plt.legend()

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("../reports/bar_chart.png")
plt.show()


# In[18]:


from matplotlib.patches import Patch

plt.figure(figsize=(8,5))

plt.hist(df["Age"].dropna(), bins=5, edgecolor="black")

plt.legend(handles=[Patch(label="Employee Age")])

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("../reports/histogram.png")
plt.show()


# In[19]:


plt.figure(figsize=(8,5))

plt.scatter(df["Age"], df["Salary"],label ="Employees")
plt.legend()

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.tight_layout()
plt.savefig("../reports/scatter.png")
plt.show()


# In[20]:


plt.figure(figsize=(8,5))

plt.plot(df["Name"], df["Salary"], marker="o",label="Employee Salary")
plt.legend()

plt.title("Employee Salary Comparison")
plt.xlabel("Employee Name")
plt.ylabel("Salary")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("../reports/line_chart.png")
plt.show()


# In[21]:


# Dataset Information
print("Dataset Information:")
df.info()

# Statistical Description
print("\nStatistical Description:")
display(df.describe())

# Display using loc
print("\nUsing loc:")
display(df.loc[0:4])

# Display using iloc
print("\nUsing iloc:")
display(df.iloc[0:5])

# Filter IT Department Employees
print("\nIT Department Employees:")
display(df[df["Department"] == "IT"])


# In[22]:


# Create departments dataset

departments = pd.DataFrame({
    "Department": ["Sales", "HR", "IT", "Finance", "Marketing"],
    "Head": ["Ramesh", "Priya", "Arun", "Kumar", "Divya"],
    "Budget": [500000, 300000, 800000, 600000, 400000]
})

# Display departments
print("Departments Dataset:")
display(departments)

# Save as CSV
departments.to_csv("../data/departments.csv", index=False)

print("departments.csv created successfully!")


# In[23]:


# Load departments CSV
departments = pd.read_csv("../data/departments.csv")

# Department-wise employee count, average and maximum salary
department_summary = df.groupby("Department").agg(
    Employee_Count=("Employee_ID", "count"),
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max")
)

print("Department Summary:")
display(department_summary)

# Inner Join
inner_join = pd.merge(df, departments, on="Department", how="inner")

print("Inner Join:")
display(inner_join)

# Left Join
left_join = pd.merge(df, departments, on="Department", how="left")

print("Left Join:")
display(left_join)

# Outer Join
outer_join = pd.merge(df, departments, on="Department", how="outer")

print("Outer Join:")
display(outer_join)


# In[24]:


get_ipython().run_line_magic('timeit', 'df["Salary"].mean()')


# In[ ]:




