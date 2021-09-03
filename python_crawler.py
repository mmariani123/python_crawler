#!/usr/bin/env Python3

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:42:02 2021

@author: Mike_2
"""

#check out https://www.blog.datahut.co/post/how-to-build-a-web-crawler-from-scratch
#for more info, they used the scrapy module so I will use it here as well. 

import scrapy
import pymongo
import os
import mysql.connector
import pymssql
import pyodbc

#For a nice ASCII code generator:
#https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

programLogo = """\n                                                                                            
             __                            _     _                                      
| | _ |_    /   __ _     |  _  __  \   /  /|    / \                                          
|^|(/_|_)   \__ | (_|\^/ | (/_ |    \_/    |  o \_/

copyright 2021 Mariani Systems LLC\n                                                                                                       
"""

inputPrompt = programLogo + "Welcome to python crawler v1.0\n" \
    "This program is usefule for web scraping and\n" \
    "SQL and MongoDB databasing\n" \
    "enter 'exit' to exit or 'help' for help\n" \
    "enter 'stats' to review the stats test\n" \
    "enter 'crawler' to use the web crawler\n" \
    "enter 'sql' or 'mongo' for interacting with databases\n" \
    "enter your command below \n" \
    + "> "
    
helpStatement="---HELP---\n press 'enter' to continue\n"

inputIn=""

crawlerMode=False

while(inputIn!="exit"):
    if inputIn=="help":
        print(helpStatement)
        input()
        inputIn=""
        os.system('cls') #use 'clear' instead of 'cls' if windows
        continue
    elif inputIn=="stats":
        print("Welcome to the stats review test\n" \
              "press enter to move through the questions\n" \
              "type 'exit' and enter at any point to exit the review\n")
        #Question 1
        statsInput=input("What is the definition of p-value?\n")
        if statsInput=='exit':
            inputIn=""
            os.system('cls') #use 'clear' instead of 'cls' if windows
            continue
        print("The Defintion of p-value is ... \n")
        #Question 2
        statsInput=input("What is the definition of statistical power?\n")
        if statsInput=='exit':
            inputIn=""
            os.system('cls') #use 'clear' instead of 'cls' if windows
            continue
        print("The Defintion of p-value is ... \n")
        #Question 3
        statsInput=input("What is faster, using a hashed array or iterating "\
                          "over a sorted array?\n")
        if statsInput=='exit':
            inputIn=""
            os.system('cls') #use 'clear' instead of 'cls' if windows
            continue
        print("The Defintion of p-value is ... \n")
        #Question 4
        statsInput=input("What is a segmentation fault (seg fault)?\n")
        if statsInput=='exit':
            inputIn=""
            os.system('cls') #use 'clear' instead of 'cls' if windows
            continue
        print("The Defintion of p-value is ... \n")
        #Question 5
        statsInput=input("Is there a faster way to find the median " \
                          "then simple sorting?\n")
        if statsInput=='exit':
            inputIn=""
            os.system('cls') #use 'clear' instead of 'cls' if windows
            continue
        print("The Defintion of p-value is ... \n")
        #Question 6
        statsInput=input("How would you detetmine if a distribution is " \
                          "normal (e.g. is there a particular bespoke test?\n")
        if statsInput=='exit':
            inputIn=""
            os.system('cls') #use 'clear' instead of 'cls' if windows
            continue
        print("The Defintion of p-value is ... \n")
        #Question 7
        statsInput=input("How would you compare two distributions to" \
                          "establish if they are identical?\n")
        if statsInput=='exit':
            inputIn=""
            os.system('cls') #use 'clear' instead of 'cls' if windows
            continue
        print("The Defintion of p-value is ... \n")
        #Question 8
        statsInput=input("How would you determine goodness of fit for " \
                          "a distribution?\n")
        if statsInput=='exit':
            os.system('cls') #use 'clear' instead of 'cls' if windows
            inputIn=""
            continue
        print("The Defintion of p-value is ... \n")
        #Question 9
        statsInput=input("Why/when do we use multiple test correction?\n")
        if statsInput=='exit':
            inputIn=""
            os.system('cls') #use 'clear' instead of 'cls' if windows
            continue
        print("The Defintion of p-value is ... \n")
        #Question 10
        statsInput=input("What is principle component analysis and "\
                          "when would one use binomial clustering?\n")
        if statsInput=='exit':
            inputIn=""
            os.system('cls') #use 'clear' instead of 'cls' if windows
            continue
        print("The Defintion of p-value is ... \n")
        print("Stats test complete!\n")
        inputIn=""
        os.system('cls') #use 'clear' instead of 'cls' if windows
        continue
    elif inputIn=="crawler":
        crawlerMode=True
        while(crawlerMode):
            crawlerInput = input("You are now in crawler mode\n " \
                                 "type 'exit' at anytime to return "\
                                 "to the the main menu\n" \
                                 "crawler> ")
            if(crawlerInput=="exit"):
                crawlerMode=False
                inputIn=""
                os.system('cls') #use 'clear' instead of 'cls' if windows
                continue
            else:
                print("Execute crawler command\n")
                #class spider1(scrapy.Spider):
                #    name = ‘Wikipedia’
                #    start_urls = [‘https://en.wikipedia.org/wiki/Battery_(electricity)’]       
                #    def parse(self, response):
                #        pass
    elif inputIn=="sql":

        #mycursor.execute("CREATE DATABASE mydatabase")
        #print(mydb)
        #import pyodbc 
        #conn = pyodbc.connect('Driver={SQL Server};'
        #              'Server=localhost\SQLEXPRESS;'
        #              'Database=myDatabase;'
        #              'Trusted_Connection=yes;')
        #csr = conn.cursor()  
        #csr.close()
        #conn.close()     #<--- Close the connection
        #You can check if a database exist by listing all databases 
        #in your system by using the "SHOW DATABASES" statement:
        
        def connect():
            """ Connect to MySQL database """
            conn = None
            try:
                conn = mysql.connector.connect(
                    host = '127.0.0.1',
                    port = '3306',
                    user = 'mike',
                    passwd = 'capncrunch1',
                    db = 'myDatabase'
                    connection_timout=300
                )
                if conn.is_connected():
                    print('Connected to MySQL database')
            except Error as e:
                print(e)
            finally:
                if conn is not None and conn.is_connected():
                    conn.close()
                    
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mydatabase"
            )
        if mydb.is_connected():
            print('Connected to MySQL database')
            print(mydb)
        
        mycursor = mydb.cursor()

        mycursor.execute("SHOW DATABASES")

        for x in mycursor:
            print(x)
            
        mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
  
        mycursor.execute("SHOW TABLES")

        for x in mycursor:
            print(x)
            
        #When creating a table, you should also create 
        #a column with a unique key for each record.
        #This can be done by defining a PRIMARY KEY.

        #We use the statement "INT AUTO_INCREMENT PRIMARY KEY" 
        #which will insert a unique number for each record. 
        #Starting at 1, and increased by one for each record.
        
        #If the table already exists, use the ALTER TABLE keyword:        
        
        #mycursor.execute("ALTER TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

        mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
        
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        mycursor.execute(sql, val)

        mydb.commit()
        
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = [
            ('Peter', 'Lowstreet 4'),
            ('Amy', 'Apple st 652'),
            ('Hannah', 'Mountain 21'),
            ('Michael', 'Valley 345'),
            ('Sandy', 'Ocean blvd 2'),
            ('Betty', 'Green Grass 1'),
            ('Richard', 'Sky st 331'),
            ('Susan', 'One way 98'),
            ('Vicky', 'Yellow Garden 2'),
            ('Ben', 'Park Lane 38'),
            ('William', 'Central st 954'),
            ('Chuck', 'Main Road 989'),
            ('Viola', 'Sideway 1633')
            ]   

        mycursor.executemany(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "was inserted.")

        #You can get the id of the row you just 
        #inserted by asking the cursor object.

        #Note: If you insert more than one row, 
        #the id of the last inserted row is returned.

        print(mycursor.rowcount, "record inserted.")

        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = ("Michelle", "Blue Village")
        mycursor.execute(sql, val)

        mydb.commit()

        print("1 record inserted, ID:", mycursor.lastrowid)

        mycursor.execute("SELECT * FROM customers")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
            
        mycursor.execute("SELECT name, address FROM customers")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
            
        mycursor.execute("SELECT * FROM customers")
        
        myresult = mycursor.fetchone()
        
        print(myresult)
        
        sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
  
        inputIn=""
        os.system('cls') #use 'clear' instead of 'cls' if windows
        continue
    
    elif inputIn=="mongo":
        #https://checkinnuggets.wordpress.com/2019/10/29/creating-a-windows-firewall-for-mongodb-or-other-programs-for-that-matter/
        #Note I made windows firewall rule for inbound allowance on port 27017
        #and named it _MongoDB
        #Note keeping the defailt db name 'myFirstDatabase' seems to work.
        #although myFirstDatabase does not seem to be a database, what's
        #going on here?
        myclient = pymongo.MongoClient("mongodb+srv://mike:capncrunch1@cluster0.vhw47.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = myclient.test
        print(db)
        print("")
        dblist = myclient.list_database_names()
        print(dblist)
        print("")
        if "sample_airbnb" in dblist:
            print("The database exists.\n")
        else:
            print("The database DOES NOT exist.\n")
        mydb = myclient["mydatabase"]
        myCollection = mydb["customers"]
        print(mydb.list_collection_names())
        print("\n")
        
        collectionList = mydb.list_collection_names()
        if "customers" in collectionList:
            print("The collection exists.")
        else:
            print("the collection DOES NOT exist.")
        #Remember, the collection does not exist until it has content.
        mydict = { "name": "John", "address": "Highway 37" }
        #x = myCollection.insert_one(mydict)
        mydict = { "name": "Peter", "address": "Lowstreet 27" }
        #x = myCollection.insert_one(mydict)
        #Note that a record is called a document in mongodb
        #print(x.inserted_id)
        mylist = [
                    { "name": "Amy", "address": "Apple st 652"},
                    { "name": "Hannah", "address": "Mountain 21"},
                    { "name": "Michael", "address": "Valley 345"},
                    { "name": "Sandy", "address": "Ocean blvd 2"},
                    { "name": "Betty", "address": "Green Grass 1"},
                    { "name": "Richard", "address": "Sky st 331"},
                    { "name": "Susan", "address": "One way 98"},
                    { "name": "Vicky", "address": "Yellow Garden 2"},
                    { "name": "Ben", "address": "Park Lane 38"},
                    { "name": "William", "address": "Central st 954"},
                    { "name": "Chuck", "address": "Main Road 989"},
                    { "name": "Viola", "address": "Sideway 1633"}
                ]
        #x = myCollection.insert_many(mylist)
        #print list of the _id values of the inserted documents:
        #print(x.inserted_ids)
        #Remember that the values has to be unique. 
        #Two documents cannot have the same _id.
        mylist = [
                    { "_id": 1, "name": "John", "address": "Highway 37"},
                    { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
                    { "_id": 3, "name": "Amy", "address": "Apple st 652"},
                    { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
                    { "_id": 5, "name": "Michael", "address": "Valley 345"},
                    { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
                    { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
                    { "_id": 8, "name": "Richard", "address": "Sky st 331"},
                    { "_id": 9, "name": "Susan", "address": "One way 98"},
                    { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
                    { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
                    { "_id": 12, "name": "William", "address": "Central st 954"},
                    { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
                    { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
                ]
        #x = myCollection.insert_many(mylist)
        #print list of the _id values of the inserted documents:
        #print(x.inserted_ids)
        
        x = myCollection.find_one()
        print(x)
        print("\n")
        
        for x in myCollection.find():
            print(x)
  
        print("\n")
  
        for x in myCollection.find({},{ "_id": 0, "name": 1, "address": 1 }):
            print(x)
        
        print("\n")
        
        for x in myCollection.find({},{ "address": 0 }):
            print(x)
            
        #The below will throw an error because you are not allowed 
        #to include both 0s and 1s in an object, unless the 0 is in the 'id'
        #field
        #for x in myCollection.find({},{ "name": 1, "address": 0 }):
        #    print(x)
            
        #A document in MongoDB is the same as a record in SQL databases
        #myclient = pymongo.MongoClient(mongodb://mike.example.com:27017
        #mydb = myclient["cluster0"]
        #print(client.list_database_names())
        
        myquery = { "address": "Park Lane 38" }
        mydoc = myCollection.find(myquery)
        for x in mydoc:
            print(x)
            print("\n")
        
        #Use quert modifiers to find letters greater than 'S'
        myquery = { "address": { "$gt": "S" } }
        mydoc = myCollection.find(myquery)
        for x in mydoc:
            print(x)
            print("\n")
            
        myquery = { "address": { "$regex": "^S" } }
        mydoc = myCollection.find(myquery)
        for x in mydoc:
            print(x)
            print("\n")
            
        mydoc = myCollection.find().sort("name")
        for x in mydoc:
            print(x)
            print("\n")
  
            
        #print "customers" after the update:
        for x in myCollection.find():
            print(x)
        #sort("name", 1) #ascending
        #sort("name", -1) #descending
        
        mydoc = myCollection.find().sort("name", -1)
        for x in mydoc:
            print(x)
            print("\n")
            
        myquery = { "address": "Mountain 21" }
        myCollection.delete_one(myquery)
        
        myquery = { "address": {"$regex": "^S"} }
        x = myCollection.delete_many(myquery)
        print(x.deleted_count, " documents deleted.")
        print('\n')
        
        x = myCollection.delete_many({})
        print(x.deleted_count, " documents deleted.")
        print('\n')
                
        yquery = { "address": "Valley 345" }
        newvalues = { "$set": { "address": "Canyon 123" } }
        myCollection.update_one(myquery, newvalues)
        #print "customes" after the update:
        print('\n')
        for x in myCollection.find():
            print(x)
            print('\n')
            
        myquery = { "address": { "$regex": "^S" } }
        newvalues = { "$set": { "name": "Minnie" } }
        x = mycol.update_many(myquery, newvalues)
        print(x.modified_count, "documents updated.")
            
        myresult = myCollection.find().limit(5)
        #print the result:
        for x in myresult:
            print(x)
            print('\n')
        
        #You can delete a table, or collection as it is called in MongoDB, 
        #by using the drop() method.
        myCollection.drop()
        
        inputIn=""
        os.system('cls') #use 'clear' instead of 'cls' if windows
        continue
    else:
        inputIn = input(inputPrompt)
        #print(inputIn)
else:
    print("Thank you for using python crawler v1.0, thank you!\n")
