from unittest import result
import flask
from flask import Flask, request, render_template, redirect
import sqlite3

from sqlalchemy import Result

conn = sqlite3.connect("studentmanagement.db", check_same_thread=False)
cursor = conn.cursor()

listOfTables= conn.execute("SELECT name from sqlite_master WHERE type='table' AND name='STUDENT' ").fetchall()

if listOfTables!=[]:
    print("Table Already Exists ! ")
else:
    conn.execute(''' CREATE TABLE STUDENT(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT, Admno INTEGER, College TEXT, Branch TEXT,   
                            DOB INT, Email TEXT, Password TEXT); ''')
print("Table has created")

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def studentadd():

    if request.method == "POST":
        getname = request.form["name"]
        getadmno = request.form["admno"]
        getcollege = request.form["college"]
        getbranch = request.form["branch"]
        getDOB = request.form["DOB"]
        getusername = request.form["Email"]
        getpassword = request.form["password"]

        print(getname)
        print(getadmno)
        print(getcollege)
        print(getbranch)
        print(getDOB)
        print(getusername)
        print(getpassword)
        try:
            conn.execute("INSERT INTO STUDENT(name, Admno, College, Branch, DOB, Email, Password)VALUES('"+getname+"','"+getadmno+"','"+getcollege+"','"+getbranch+"','"+getDOB+"','"+getusername+"','"+getpassword+"')")
            print("SUCCESSFULLY INSERTED!")
            conn.commit()
            return redirect('/viewall')
        except Exception as e:
            print(e)

    return render_template("student.html")

@app.route("/search", methods =['GET','POST'])
def search():
    if request.method == "POST":
        getadmno = request.form["admno"]
        print(getadmno)
        try:
            query = "SELECT * FROM STUDENT WHERE Admno="+getadmno
            print(query)
            cursor.execute(query)
            print("SUCCESSFULLY SELECTED!")
            result = cursor.fetchall()
            print(result)
            if len(result) == 0:
                print("Invalid Admission number")
            else:
                print(len(result))
                return render_template("search.html", stud=result, status = True)

        except Exception as e:
            print(e)

    return render_template("search.html", stud=[], status = False)

@app.route("/delete", methods =['GET','POST'])
def delete():
    if request.method == "POST":
        getadmno = request.form["admno"]
        print(getadmno)
        try:
            conn.execute("DELETE FROM STUDENT WHERE Admno="+getadmno)
            print("SUCCESSFULLY DELETED!")
            result = cursor.fetchall()
        except Exception as e:
            print(e)
    return flask.render_template("delete.html")

@app.route("/update", methods = ['GET','POST'])
def update():
    if request.method == "POST":
        getadmno = request.form["admno"]
        print(getadmno)
        try:
            cursor.execute("SELECT * FROM STUDENT WHERE Admno="+getadmno)
            print("SUCCESSFULLY SELECTED!")
            if len(Result) == 0:
                print("Invalid Admission number")
            else:
                print(len(result))
                return render_template("update.html", stud=result)
            return redirect("/viewupdate")
        except Exception as e:
            print(e)

    return render_template("update.html")

@app.route("/viewupdate", methods = ['GET','POST'])
def viewupdate():
    if request.method == "POST":
        getname = request.form["name"]
        getadmno = request.form["admno"]
        getcollege = request.form["college"]
        getbranch = request.form["branch"]
        getDOB = request.form["DOB"]
        getusername = request.form["Email"]
        getpassword = request.form["password"]

        print(getname)
        print(getadmno)
        print(getcollege)
        print(getbranch)
        print(getDOB)
        print(getusername)
        print(getpassword)
        try:
            conn.execute("UPDATE INTO STUDENT(name, Admno, College, Branch, DOB, Email, Password)VALUES('"+getname+"','"+getadmno+"','"+getcollege+"','"+getbranch+"','"+getDOB+"','"+getusername+"','"+getpassword+"')")
            print("SUCCESSFULLY UPDATED!")
            conn.commit()
            return redirect('/viewall')
        except Exception as e:
            print(e)

    return render_template("viewupdate.html")

@app.route("/viewall")
def viewall():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STUDENT")
    result = cursor.fetchall()
    return render_template("viewall.html",students=result)

@app.route("/cardview")
def cardview():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STUDENT")
    result = cursor.fetchall()
    return render_template("cardview.html",students=result)

if(__name__) == "__main__":
    app.run()