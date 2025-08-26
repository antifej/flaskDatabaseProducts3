# connecting to Api server to get cat Gif URL
import requests



catGifURL= "https://api.thecatapi.com/v1/images/search"

def getRandomCatURL():
    connection = requests.get(catGifURL)
    if connection.status_code == 200:
        print("Connection is successfull! ", connection.status_code)

        jsonData = connection.json()
        print(jsonData)

        catURL = jsonData[0]["url"]
        return catURL

    else:
        print("Bad connection! ", connection.status_code)
        return ""



