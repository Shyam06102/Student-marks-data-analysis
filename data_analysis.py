# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create Dataset

data = {
    "Name": ["Arun", "Bala", "Chitra", "Divya", "Karthik"],
    "Maths": [78, 85, 90, 70, 88],
    "Science": [82, 79, 88, 75, 91],
    "English": [80, 83, 85, 72, 87]
}

# Create DataFrame

df = pd.DataFrame(data)

# Display Dataset

print("Dataset:")
print(df)

# Data Cleaning (Check Missing Values)

print("\nMissing Values:")
print(df.isnull().sum())

# Statistical Analysis

print("\nStatistical Summary:")
print(df.describe())

# Calculate Average Marks

df["Average"] = np.mean(df[["Maths", "Science", "English"]], axis=1)

print("\nAverage Marks:")
print(df[["Name", "Average"]])

# Find Highest Marks

highest = df[["Maths", "Science", "English"]].max()

print("\nHighest Marks in Each Subject:")
print(highest)

# Bar Chart (Average Marks)

plt.bar(df["Name"], df["Average"])
plt.title("Average Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.show()

# Line Graph (Subject Comparison)

plt.plot(df["Name"], df["Maths"], marker='o')
plt.plot(df["Name"], df["Science"], marker='o')
plt.plot(df["Name"], df["English"], marker='o')

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend(["Maths", "Science", "English"])
plt.show()
