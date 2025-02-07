import pandas as pd

# Create sample DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
df3 = pd.DataFrame({'A': [1, 2, 4], 'B': ['x', 'y', 'z']})

#compaeing the data Frames
print("df1 equals df2:", df1.equals(df2))  # True
print("df1 equals df3:", df1.equals(df3))  # False

#comparing if df1 and df3 are equal or not
comparison_df = df1 == df3
print("Element-wise Comparison:")
print(comparison_df)

# Find differences
diff_df = df1[df1 != df3]
print("Differences between df1 and df3:")
print(diff_df)




#Most simple method
comparison_result = df1.compare(df3)
print("Comparison Result:")
print(comparison_result)