def listUpt(CityList):
    for i in range(len(CityList)):
        CityList[i] = i  
    return CityList

cities = ["Athens", "Thessaloniki", "Patra"]

print(listUpt(cities))  
