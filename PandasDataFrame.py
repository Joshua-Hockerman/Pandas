import pandas as pd

grades_dict = {
    "Wally": [87, 96, 70],
    "Eva": [100, 87, 90],
    "Sam": [94, 77, 90],
    "Katie": [100, 81, 82],
    "Bob": [83, 65, 85],
}

grades = pd.DataFrame(grades_dict)

grades.index = ["Test 1", "Test 2", "Test 3"]

# print(grades)

# print(grades.iloc[[0, 2]])

# print(grades.loc["Test 1"])

# print(grades.loc["Test 1":"Test 2", ["Eva", "Katie"]])

# grades90 = grades[grades >= 90]

# print(grades90)

# gradesB = grades[(grades >= 80) & (grades < 90)]

# print(gradesB)

# gradesAorC = grades[(grades >= 90) | ((grades >= 70) & (grades < 90))]

# print(gradesAorC)

# print(grades.at["Test 2", "Eva"])

# print(grades.iat[1, 1])

# print(grades.describe())

pd.set_option("precision", 2)

print(grades.describe())

print(grades.T.describe())

print(grades.sort_index(ascending=False))

print(grades.sort_index(axis=1))

print(grades.sort_values(by="Test 1", axis=1, ascending=False))

print(grades.loc["Test 1"].sort_values(ascending=False))
