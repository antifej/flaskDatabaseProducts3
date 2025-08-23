import sqlite3

databaseName = "Products.db"

def getData(query):
    try:

        connection=sqlite3.connect(databaseName)
        cursor = connection.cursor()

        cursor.execute(query)


        data=cursor.fetchall()
        connection.close()
        print(data)
        return data

    except Exception as e:
        print(e.__str__())
        return ""



#getData(query)