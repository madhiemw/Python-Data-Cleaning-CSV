import pandas as pd 

data  = pd.read_csv(r'C:\Users\DIDAN\OneDrive\Documents\kandedes\dirtydata.csv')
data["Calories"].fillna(130, inplace = True)
print (data)
x = data["Calories"].mean()
z = data["Calories"].median()
y = data["Calories"].mode()[0]
data['Date'] = pd.to_datetime(data['Date']) # fixing date format in the Row
data.dropna(subset=['Date'], inplace= True) # auto delete for entire row 
data.loc[7,'Duration'] = 45 # fixing Duration's data row number 7
for x in data.index: # looping for automatically change a value in a column if it has > our decide value
  if data.loc[x, "Duration"] > 120:
    data.loc[x, "Duration"] = 120
for x in data.index:         # looping for automatically delete entire row if it has > our decide value
  if data.loc[x, "Duration"] > 59:
       data.drop(x, inplace = True)
print(data.duplicated())
data.drop_duplicates(inplace= True )
print(data.to_string())
