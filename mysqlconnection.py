#first we need to create database in mysql workbench so that we should establish the connection.
#then check whether connection is success or not
#then perform curd operation
#create four function insert,select,delete,update
#use mysql query to connect database
#then ask user to input values and perform actions

from tabulate import tabulate #import package pip install tabulate
import mysql.connector # import package pip install mysql-connector-python

con = mysql.connector.connect(host="localhost",user="root", password="Admin",database="mydb") # to check our database connection

if con:
    print("connected")
else:
    print("error")


def select(): # to display function
    connection = con.cursor()
    qry = "select * from student_details"
    connection.execute(qry)
    display = connection.fetchall()
    print(tabulate(display,headers=("ID","Student_Name","Class","Fees")))
    con.commit()
def insert(name,cls,fees): # to Insert function
    connection = con.cursor()
    qry = "insert into student_details (name,class,fees) values(%s,%s,%s)"
    queries=(name,cls,fees)
    connection.execute(qry,queries)
    print("Record Added")
    con.commit()
def update(name,cls,fees,id): # to update function
    connection = con.cursor()
    qry = "update student_details set name=%s,class=%s,fees=%s where id =%s"
    queries=(name,cls,fees,id)
    connection.execute(qry,queries)
    print("Record Modify")
    con.commit()
def delete(id): # to delete function
    connection = con.cursor()
    qry = "delete from student_details where id=%s"
    queries=(id,)
    connection.execute(qry,queries)
    print("Record deleted")

msg = """
1. Display student details
2. Add New student details
3. Update Existing student details
4. Delete student record
5. Exit
"""

while True:
    print(msg)
    try:
        choice = int(input("Enter the Choices :"))
        if choice == 1:
            try:
                select()
            except Exception as e:
                print("unable to view the records")
        elif choice ==2:
            try:
                name = input("Enter the Name :")
                cls = input ("Class :")
                fees = input("Are you payed your term fees yes or no :").lower()
                def result(x):
                    if x == "yes":
                        replace = x.replace("yes","Payed")
                        return replace
                    elif x == "no":
                        replace = x.replace("no","Pending")
                        return replace    
                insert(name,cls,result(fees))
            except Exception as e:
                print("unable to Add the records")
        elif choice ==3:
            try:
                id = int(input("Which student id record you want to modify :"))
                name = input("Enter the Name :")
                cls = input ("Class :")
                fees = input("Are you payed your term fees yes or no :").lower()
                def result(x):
                    if x == "yes":
                        replace = x.replace("yes","Payed")
                        return replace
                    elif x =="no":
                        replace = x.replace("no","Pending")
                        return replace    
                update(name,cls,result(fees),id)
            except Exception as e:
                print("unable to Edit the records")
        elif choice ==4:
            try:
                id = int(input("Enter student id to remove the records :"))
                delete(id)
            except Exception as e:
                print("unable to delete the records")
        elif choice ==5:
            print("Database Closed")
            exit()
    except Exception as e:
        print("Invalid Choices")
