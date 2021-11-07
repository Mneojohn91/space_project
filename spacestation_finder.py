import pandas as pd
import numpy as np
import plotly.express as px

url='http://api.open-notify.org/iss-now.json'
df=pd.read_json(url)
df['latitude']=df.loc['latitude','iss_position']
df['longitude']=df.loc['longitude','iss_position']
df.reset_index(inplace=True)
df=df.drop(['index','message'],axis=1)

figure=px.scatter_geo(df,lat='latitude',
                      lon='longitude')
figure.show()

