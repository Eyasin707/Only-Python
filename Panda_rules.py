#today is Panda dayyyy! Let's learn panda from python.

#Let's begin by creating a simple and basic dataset using data structure-List.
import pandas as pd
my_list=["car", "house", "guns"]
my_dataset= pd.Series(my_list)
print(my_dataset)

#let's label our data:
my_list=["car", "house", "guns"]
my_dataset= pd.Series(my_list, index=["January_cost","Feb_cost","March_cost"])
print(my_dataset)

#let's create an dict. to turn into dataset:
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
df.index=[1,2,3,4,5,6]   #To edit rows aka indexes
print(df) 

#This far we were creating only 1D dataframes. It's time to hop into multidimensionals:

'''
list_2=["car", "house", "guns"]
dict_2={
    "car": "BMW",
    "House": "WOW",
    "NAME": "SAM"
}
combined_dataframe= {
    "list_2": list_2,
    "dict_2": dict_2
}
combined_dataframe_4=pd.DataFrame(combined_dataframe)
print(combined_dataframe_4)
'''
#In the above thing it's not possible directly combine dict and list. Later check out what can be done.

#A simple 2D dataframe:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)             #first create the obj.
df.index= ["jan", "feb" , "march"] #Then edit it
df.columns=["D for Duratoin", "P for pulse"]
print(df) 
