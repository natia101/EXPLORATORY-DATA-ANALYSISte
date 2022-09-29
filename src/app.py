import pandas as pd

from utils import db_connect
engine = db_connect()

# Importación de datos

url = 'https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/' + \
      'main/AB_NYC_2019.csv'
df = pd.read_csv(url)

# Transformación de datos

df=df.astype({'name':'str','host_name':'str','neighbourhood_group':'category','neighbourhood':'category','room_type':'category'})
df['last_review'] = pd.to_datetime(df['last_review'], format="%Y/%m/%d")

# Limpieza de datos


aux=df.groupby('neighbourhood_group')['price'].agg(['mean'])
new_price=[]
for i,r in df[['price']].iterrows():
    if r['price']==0:
        new_price.append(aux.loc[df['neighbourhood_group'][i],'mean']) # precio medio del area
    else :
        new_price.append(r['price'])
df['price']=new_price

df=df[df['minimum_nights']<750] 

# Exportacion de la base procesada
df.to_csv('/workspace/EXPLORATORY-DATA-ANALYSISte/data/processed/Data.csv') 