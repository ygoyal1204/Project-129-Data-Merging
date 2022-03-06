import pandas as pd

df = pd.read_csv("dwarf_stars.csv")

#Deleting NAN values
df = df.dropna()

#Coverting mass column to floating point values
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

#Coverting radius and mass column to solar radius and solar mass
df["Radius"] = 0.102763*df["Radius"]
df["Mass"] = 0.000954588*df["Mass"]

df.drop(['Unnamed: 0'], axis=1, inplace=True)
df.reset_index(drop=True,inplace=True)

df.to_csv("unit_coverted_stars.csv")

