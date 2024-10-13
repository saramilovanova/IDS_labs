import pandas as pd

print("Hello")

df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
print(df)

df.to_excel('Book_1.xlsx', index=False)

