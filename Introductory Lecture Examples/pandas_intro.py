import pandas as pd

data = { "name": ["ali", "mehmet", "ayse"],
         "midterm": [21, 28, 31],
         "final": [90, 54, 71],
         "attendance": [6, 10, 17]}

df_student = pd.DataFrame(data)

# Broadcasting
df_student["total"] = 0

# Column Calculating
df_student["total"] = (df_student["midterm"] * 0.3) + df_student["final"] * 0.7
df_student.loc[(df_student["total"] > 47, 'grade')] = "A"
print(df_student.loc[0])

