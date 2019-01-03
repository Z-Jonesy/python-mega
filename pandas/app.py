import pandas
import geopy
from geopy.geocoders import ArcGIS
nom = ArcGIS()
#df=pandas.read_csv("supermarkets.csv")
#df["Address_2"]=df["Address"]+","+df["City"]+","+df["State"]+","+df["Country"]

df=pandas.read_csv("customers.csv")
df["Address_2"]=df["Address"].apply(str)+","+df["Zip"].apply(str)+","+df["City"].apply(str)+","+df["Country"].apply(str)

df["Coordinates"]=df["Address_2"].apply(nom.geocode)

df["Lat"]=df["Coordinates"].apply(lambda x: x.latitude if x!=None else None)
df["Lon"]=df["Coordinates"].apply(lambda x: x.longitude if x!=None else None)

df.to_csv("out.csv")
