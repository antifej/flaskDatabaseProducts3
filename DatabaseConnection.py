import sqlite3

databaseName = "products.db"


def createNewUser(username, password, isAdmin):
    query = "Insert into Users (username, password, isadmin) values ('"+username+"', '"+password+"',"+str(isAdmin)+" );"
    try:
        connection =sqlite3.connect(databaseName)
        cursor = connection.cursor()
        cursor.execute(query)

        connection.commit()
        connection.close()
        return username +" added to database !"
    except Exception as e:
        return "Failed " +e.__str__()

#result = createNewUser("Alex", "123",0)
#print(result)



def deleteAlcoholRecord(id):
    query = "Delete from Alcohol where id = "+str(id)+";"
    try:
        connection = sqlite3.connect(databaseName)
        cursor = connection.cursor()
        cursor.execute(query)

        connection.commit()
        connection.close()
        print(id, "deleted from database")
    except Exception as e:
        print(e.__str__())

##deleteAlcoholRecord(32)





def addNewAlcohol(name, url,degre,price, isDiscount ):
    query = "Insert into Alcohol(name, img_url,degre,price,discount) values ('"+name+"', '"+url+"', "+str(degre)+", "+str(price)+", "+str(isDiscount)+");"
    try:
        connection = sqlite3.connect(databaseName)
        cursor = connection.cursor()
        cursor.execute(query)

        connection.commit()
        connection.close()
        print(name + "added to database")
    except Exception as e:
        print(e.__str__())

#addNewAlcohol("Cocola", "...", 12, 1.56, 0)


def getData(query):
    try:

        connection =sqlite3.connect(databaseName)
        cursor = connection.cursor()

        cursor.execute(query)


        data = cursor.fetchall()
        connection.close()
        print(data)
        return data


    except Exception as e:
        print(e.__str__())
        return  ""



#getData(query)

