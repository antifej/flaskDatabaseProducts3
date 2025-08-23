#Python Dictionary = JSON
carBrands = ["Nissan", "Toyota", "Mitsubishi", "Tesla"]
print(carBrands[1])

carMarket = {"Adres":"Bauskas street 22",
             "CarCount":245,
             "Total Tax": 1455.6,
             "isWorking":True,
             "CarModelsToSell":["Ford", "Fiat", "Audi", "Subaru"]}

print("Car market total tax is ", carMarket["Total Tax"])
print("Car market type is ", type(carMarket))

#2 car model that is selling

print(carMarket["CarModelsToSell"][1])
print("All keys in carMarket ", carMarket.keys())

print("All key values ", carMarket.values())


personDictionary ={"Person1":{"Name":"Alex", "Age": 34, "IsLucky": False, "Weight":86.3},
                   "Person2":{"Name":"Marta", "Age": 27, "IsLucky": True, "Weight":62},
                   "Person3":{"Name":"Ilze", "Age": 12, "IsLucky": True, "Weight":32},
                   "Person4":{"Name":"Samanta", "Age": 19, "IsLucky": False, "Weight":48},
                   }

#1. Write full information about Person3
#2. Get full age of all persons
#3. Get Person1 Weight
#4. Print all person names
#5. Print only Lucky persons
#6. Print oldest person
#7. Print youngest person

