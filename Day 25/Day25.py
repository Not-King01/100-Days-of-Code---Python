
'''
import csv
with open("weather_data.csv", "r") as data_value:
    data = csv.reader(data_value)
    temperature = []

    for values in data:
        if values[1] != 'temp':
            temperature.append(int(values[1]))
        
print(temperature)

'''
'''
import pandas as pd
data = pd.read_csv("weather_data.csv")

# Get data in a row
monday = data[data.day == "Monday"]
print(monday.temp)
print((9/5*monday.temp + 32))

#Create a dataframe from scratch

data_dict = {"Students": ["King", "Queen", "Prince", "Princess"],
             "Scores": [100, 95, 60, 75]}
dic = pd.DataFrame(data_dict)
print(dic)
dic.to_csv("new_data1.csv")
'''

import pandas as pd
data = pd.read_csv("Squirrel_Census.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels)
print(cinnamon_squirrels)
print(black_squirrels)

data_dict = {"Fur Color":["Gray", "Cinnamon", "Black"], "Count" : [gray_squirrels, cinnamon_squirrels, black_squirrels]}
df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")



































