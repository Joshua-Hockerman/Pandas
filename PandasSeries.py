import pandas as pd

grades = pd.Series([87, 100, 94])

##print(grades)

grades2 = pd.Series(98.6, range(3))

# print(grades2)

# print(grades[0])

# print(grades.describe())

grades = pd.Series([87, 100, 94], index=["Wally", "Eva", "Sam"])

# print(grades["Eva"])

# print(grades.Wally)

# print(grades.dtype)

# print(grades.values)

hardware = pd.Series(["Hammer", "Saw", "Wrench"])

print(hardware)

# print(hardware.str.contains("a"))

# print(hardware.str.contains('z'))

print(hardware.str.upper())
