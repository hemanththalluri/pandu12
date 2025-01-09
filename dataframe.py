import pandas as pd


data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [24, 30, 22, 28],
    'salary': [50000, 60000, 55000, 70000]
}
employees = pd.DataFrame(data)

print(employees.head(2))

employees['Bonus'] = employees['salary'] * 0.10


average_salary = employees['salary'].mean()
print(f'Average Salary: {average_salary}')


older_employees = employees[employees['age'] > 25]
print(older_employees)


import pandas as pd

# Create a DataFrame from the provided data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}

employees = pd.DataFrame(data)

# Display the DataFrame
print(employees)