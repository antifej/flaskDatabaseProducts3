#23.08.2025
# Dictionary = JSON



movieDictionary = {"Movie 1":{"Name":"Harry Potter", "Year":2001,"isForAdults": False,"Time":106.34},
                   "Movie 2":{"Name":"Lord of the Rings", "Year":2001,"isForAdults": False,"Time":176.34},
                   "Movie 3":{"Name":"Fight Club", "Year":1999,"isForAdults": True,"Time":150.12},
                   "Movie 4":{"Name":"American Psycho", "Year":2000,"isForAdults": True,"Time":102.12},
                   "Movie 5":{"Name":"Shrek", "Year":2000,"isForAdults": False,"Time":89.34},
                   "Movie theater":["Silver Screen","Forum Cinema", "Daugavpils Kultūras pils", "Plaza cinema" ]
                   }

#1. Print all movie names
#2. Print movies, that adults can only watch
#3. Print movies names, that are made after 2000 year
#4. Sort all Movie theater names by Alphabet and print them.
#5. Find the longest movie
#6. Get all movie lenght

#1
print(movieDictionary.values())
movieNumber =1
for oneValue in movieDictionary.values():
    if isinstance(oneValue,dict):
        print(f"{movieNumber}. {oneValue['Name']}")
        movieNumber+=1
#2
print("#2. Print movies, that adults can only watch")
for oneValue in movieDictionary.values():
    if isinstance(oneValue,dict):
        if oneValue["isForAdults"] == True:
            print(oneValue["Name"])

#3
print("Movies, that are made after 2000")
for oneValue in movieDictionary.values():
    if isinstance(oneValue,dict) and oneValue["Year"] > 2000:
        print(oneValue["Name"])


#4
print("Movie theater names sorted!")
for oneValue in movieDictionary.values():
    if isinstance(oneValue, list):
        oneValue.sort()
        print(oneValue)
        for oneCinema in oneValue:
            print(oneCinema)


#5
print("Longest movie name")
longestMovieName =""
longestMovieTime =0

for oneValue in movieDictionary.values():
    if isinstance(oneValue, dict) and oneValue["Time"]  > longestMovieTime:
        longestMovieTime =oneValue["Time"]
        longestMovieName = oneValue["Name"]


print(longestMovieName)

#6

print("Total Movie Length")
totalMovieLenght=0
for oneValue in movieDictionary.values():
    if isinstance(oneValue, dict):
        totalMovieLenght += oneValue["Time"]


totalMovieLenght = round(totalMovieLenght,2)
print(totalMovieLenght)


