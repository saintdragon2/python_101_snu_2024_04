import pandas as pd


arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(arr)

df = pd.DataFrame(arr, columns=['A', 'B', 'C'])

print(df)


df['sum'] = df['A'] + df['B'] + df['C']
print(df)

df['avg'] = df['sum'] / 3
print(df)


df_b = pd.DataFrame([
    [1, 'a', 'b'],
    [4, 'c', 'd'],
    [7, 'e', 'f']
], columns=['A', 'E', 'F'])

print(df_b)

df_ab = pd.merge(df, df_b, on='A', how='inner')
print(df_ab)