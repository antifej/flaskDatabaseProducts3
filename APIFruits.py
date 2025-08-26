import requests
import json


fruitURL = "https://fruityvice.com/api/fruit/all"

def getRandomFruitURL():
    connection = requests.get(fruitURL)
    if connection.status_code == 200:
        print("Connection is successfull! ", connection.status_code)

        jsonData = connection.json()
        print(jsonData)
        fruitDataArray = []
        for onefruit in jsonData:
            #print(onefruit)
            fruitDict={"id":onefruit["id"], "name":onefruit["name"], "family":onefruit["family"], "order":onefruit["order"], "genus":onefruit["genus"]}
            print(fruitDict)
            fruitDataArray.append(fruitDict)


        return fruitDataArray

    else:
        print("Bad connection! ", connection.status_code)
        return ""

getRandomFruitURL()

def getFruitById(id):
    url2 = "https://fruityvice.com/api/fruit/" +str(id)
    connection = requests.get(url2)








