# Creating the dictionary with column names as keys
students_data = {
    "Student_ID": [],
    "Name": [],
    "Subject": [],
    "Marks": [],
    "Predicted_Marks": []
}

# Adding rows of data
students_data["Student_ID"].append(1)
students_data["Name"].append("John Doe")
students_data["Subject"].append("Math")
students_data["Marks"].append(85)
students_data["Predicted_Marks"].append(90)

students_data["Student_ID"].append(2)
students_data["Name"].append("Jane Smith")
students_data["Subject"].append("Science")
students_data["Marks"].append(78)
students_data["Predicted_Marks"].append(80)

students_data["Student_ID"].append(3)
students_data["Name"].append("Emily Johnson")
students_data["Subject"].append("History")
students_data["Marks"].append(92)
students_data["Predicted_Marks"].append(95)

# Printing the dictionary
print(students_data)