#Part 1
#json file including precipitation info
import json
with open("C:\\Users\\csgb\\OneDrive\\UCU\\ACCMET2J\\Week 2\\Week2Day2\\ucaccmet2j_python\\precipitation.json") as file:
    precipitation=json.load(file)

#csv file including station info
from csv import DictReader
with open('stations.csv') as file:
    reader = DictReader(file)
    stations = list(reader)

#1.1 select measurements belonging to Seattle
seattle_measurements=[]
for measurement in precipitation:
    if measurement["station"]=="GHCND:US1WAKG0038":
        seattle_measurements.append(measurement)

#1.2 calculate total monthly precipitation for Seattle
dict_monthly_precipitation={} #create a dictionary for total monthly precipitation, with year and month as key
for measurement in seattle_measurements:
    for month in ['2010-01', '2010-02', '2010-03', '2010-04', '2010-05', '2010-06', '2010-07', '2010-08', '2010-09', '2010-10', '2010-11', '2010-12']:
        if measurement["date"].startswith(month):
            if month not in dict_monthly_precipitation:
                dict_monthly_precipitation[month]=measurement["value"]
            if month in dict_monthly_precipitation:
                dict_monthly_precipitation[month]=float(dict_monthly_precipitation[month])+float(measurement["value"])

total_monthly_precipitation_seattle=[] #turn the values from the dictionary into a list
for month in dict_monthly_precipitation:
    total_monthly_precipitation_seattle.append(dict_monthly_precipitation[month])

print(f'The total precipitation in each month in Seattle in 2010 was {total_monthly_precipitation_seattle}')

Cities = {
    "Seattle" : {
        "station":"GHCND:US1WAKG0038",
        "state":"WA",
        "total_monthly_precipitation":total_monthly_precipitation_seattle
    },
}

with open('results.json', 'w', encoding='utf-8') as file:
     json.dump(Cities, file)

#Part 2
#2.1 Calculate total yearly precipitation
total_yearly_precipitation_seattle=0
for month in total_monthly_precipitation_seattle:
    total_yearly_precipitation_seattle=total_yearly_precipitation_seattle+month

print(f'The total yearly precipitation in 2010 in Seattle was {total_yearly_precipitation_seattle}')

#2.2 Calculate relative monthly precipitation
relative_monthly_precipitation_seattle=[]
for month in total_monthly_precipitation_seattle:
    relative_monthly_precipitation_seattle.append(float(month)/float(total_yearly_precipitation_seattle))

print(f'The relative precipitation per month in Seattle in 2010 was {relative_monthly_precipitation_seattle}')

#add the new info to the dictionary
Cities["Seattle"]["total_yearly_precipitation"]=total_yearly_precipitation_seattle 
Cities["Seattle"]["relative_monthly_precipitation"]=relative_monthly_precipitation_seattle

with open('results.json', 'w', encoding='utf-8') as file:
     json.dump(Cities, file)