import requests

url = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def getDefinition(word):

    fullURL = url +word
    response = requests.get(fullURL)



    if response.status_code == 200:
        print("All well! ", response.status_code)
        jsonResponse = response.json()

        print(jsonResponse)

        definitionArrayJson = jsonResponse[0]["meanings"][0]["definitions"]

        audioLink = jsonResponse[0]["phonetics"][0]["audio"]
        print(audioLink)
        
        definitionArrayStr=[]
        
        for oneDefinition in definitionArrayJson:
            definitionArrayStr.append( oneDefinition["definition"])
            
            
        print(definitionArrayStr)

        dataToSend = {"Audio":audioLink, "DefinitionArray":definitionArrayStr}
        print(dataToSend)
        return dataToSend

    else:
        print("Bad connectione :(", response.status_code)
        return ""

#getDefinition("smile")