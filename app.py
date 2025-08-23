from flask import Flask
from flask import render_template
from DatabaseConnection import *
from flask import request
from flask import redirect
from ApiCats1 import getRandomCatURL
from APIDictionary import getDefinition

webPage = Flask(__name__)

@webPage.route("/dictionary", methods=['POST', 'GET'])
def dictionary():
    data=""


    if request.method == "POST":
        word = request.form["word"]
        data = getDefinition(word)



    return render_template("dictionary.html", data = data)




@webPage.route("/random_cat")
def randomCat():
    catURL =getRandomCatURL()
    return render_template("random_cat.html", catURL = catURL)


@webPage.route("/alcohol/<int:id>", methods=['POST', 'GET'])
def oneAlcohol(id):
    totalPay=0
    query = "Select * from Alcohol where id =" + str(id) + ";"
    oneDrink = getData(query)[0]
    daudzums =0

    if request.method == "POST":
        daudzums = request.form["daudzums"]
        totalPay = int(daudzums) * oneDrink[4]

    daudzums = int(daudzums)
    return render_template("one_alcohol.html", oneDrink=oneDrink, totalPay=totalPay, daudzums=daudzums)


@webPage.route("/add_alcohol", methods=['POST', 'GET'])
def add_alcohol():
    if request.method =="POST":
        print("Add new drink to database")
        newAlcoName = request.form["name"]
        newAlcoURL = request.form["img_url"]
        newAlcoDegre = request.form["degre"]
        newAlcoPrice = request.form["price"]

        isDicount = 0
        if request.form.__contains__("discount"):
            isDicount=1

        #newIsDiscount = request.form["discount"]
        #checkbox....
        print(newAlcoName +" " + newAlcoURL +" " +newAlcoDegre + " "+newAlcoPrice +  " ", isDicount)

        addNewAlcohol(newAlcoName,newAlcoURL,newAlcoDegre, newAlcoPrice,  isDicount)
        return redirect("/alcohol")

    else:
        return render_template("add_alcohol.html")



@webPage.route("/alcohol", methods =['POST', 'GET'])
def alchocol():
    quvery = "Select * from Alcohol order by name;"
    if request.method == "POST":
        #delete alcohol from database!
        if request.form.__contains__("drinkID"):
            drinkIDToDelete = request.form["drinkID"]
            deleteAlcoholRecord(drinkIDToDelete)

        #Check for specifik drink
        if request.form.__contains__("find"):
            print("Drink to Find ", request.form["find"])
            quvery = "Select * from Alcohol where name like '%"+request.form["find"] +"%';"

    alcoData = getData(quvery)
    return render_template("alcohol.html", alcoData=alcoData)



@webPage.route("/")
def mainRoot():
    return render_template("index.html")


@webPage.route("/all_users")
def allUsers():
    query ="Select * from Users order by username;"
    userData = getData(query)
    #print(userData)
    return render_template("all_users.html", userData = userData)


#Path for adding new users to database
@webPage.route("/register", methods=["POST", "GET"])
def register():
    message=""
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        cfpassword = request.form["cfpassword"]

        isAdmin=0
        if request.form.__contains__("isAdmin"):
            isAdmin=1

        #print("Username " + username + " password " + password + " confirm pwd " + cfpassword)
        if password != cfpassword:
            message ="PASSWORD AND CONFIRM PASSWORD DOESNT MATCH !"
        else:
            message =createNewUser(username, password,isAdmin)


    return render_template("register.html", message=message)


@webPage.route("/log_in", methods=["POST", "GET"])
def logIn():
    data=""
    if request.method == 'POST':
        userInput = request.form['username']
        pwdInput = request.form['password']

        print("user name " + userInput + 'password ' + pwdInput)

        loginQuery ="Select * from Users WHERE username = '"+userInput+"' and password = '"+pwdInput+"';"
        data = getData(loginQuery)

        if len(data) ==0:
            data="WRONG USER NAME OR PASSWORD!"
        else:
            #data = (data[0][1]).upper() + " HELLO "
            #print(data[0][3])
            if data[0][3]== 1:
                data =data[0][1].upper() + " HELLO ADMIN !"
            else:
                data =data[0][1].upper() + " HELLO USER !"

    return render_template("log_in.html", data =data)





if __name__ == "__main__":
    webPage.run(debug=True)