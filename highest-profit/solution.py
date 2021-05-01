import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)

df = pd.read_csv('data.csv')

print("Answer 1 : "+str(df.shape[0]))

df = df[pd.to_numeric(df['Profit (in millions)'], errors='coerce').notnull()]
print("Answer 2 : "+str(df.shape[0]))

df['Profit (in millions)'] = pd.to_numeric(df['Profit (in millions)'])

df.T.to_json(r'data2.json')
print("Converted filtered CSV data to JSON and saved in data.json")

print("Answer 3:")
print(df.sort_values(['Profit (in millions)'], ascending=False)[:20])
