import pandas as pd
#To not truncate the output
pd.set_option("display.max_rows", None, "display.max_columns", None)

#Import csv file into dataframe
df = pd.read_csv('data.csv')

#Print size of data frame
print("Answer 1 : Size before filtering : ", df.shape[0])

#Remove the errors with invalid profit values
df = df[pd.to_numeric(df['Profit (in millions)'], errors='coerce').notnull()]
#Print the resulting number of rows
print("Answer 2 : Size after filtering : ", df.shape[0])

#Convert the profit values to float as we need to sort them
df['Profit (in millions)'] = pd.to_numeric(df['Profit (in millions)'])


#Convert to JSON
df.T.to_json(r'data2.json')
print("Converted filtered CSV data to JSON and saved in data2.json")


#Print top 20 rows with highest profit.
print("Top 20 rows with highest profit:")
print(df.sort_values(['Profit (in millions)'], ascending=False)[:20])

