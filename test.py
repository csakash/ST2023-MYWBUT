import requests
import pandas as pd

df = pd.read_csv('kohli.csv')

def get_latitude(x):
    url = 'https://nominatim.openstreetmap.org/search/' + x +'?format=json'
    response = requests.get(url).json()
    # print(response)
    if len(response) > 0:
        return response[0]['lat']
    else:
        return 0
    
def get_longitude(x):
    url = 'https://nominatim.openstreetmap.org/search/' + x +'?format=json'
    response = requests.get(url).json()
    # print(response)
    if len(response) > 0:
        return response[0]['lon']
    else:
        return 0

df["Lat"] = df["Ground"].apply(get_latitude)  
df["Lon"] = df["Ground"].apply(get_longitude)

df.to_csv("kohlidf.csv")
# gg = get_latitude("Dhaka")
# print(gg)

print(df)
