import numpy as np
import pandas as pd




def ConvertIATAcodeToCity(df):
    
# col = df1["DepartureCity"]
# col = list(col)

# url = "https://airport-info.p.rapidapi.com/airport"
# headers = {
#     "X-RapidAPI-Key": "5eb6c314ccmsh3b593a42e1f460cp1327e4jsn4ce8adb9f999",
#     "X-RapidAPI-Host": "airport-info.p.rapidapi.com"
# }

# for i in col:    
#     querystring = {"iata": i}
#     if i==np.nan or isinstance(i,float)==True:
#         continue
#     # print(i)		
#     if len(i) > 3:
#         continue
#     response = requests.get(url, headers=headers, params=querystring)
#     parsedData = response.json()
#     print(parsedData)
#     print(i)
#     print(parsedData['city'])