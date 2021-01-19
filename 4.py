import sqlite3 as sq
import pandas as pd
import json
from pymongo import MongoClient
import mysql.connector

#Coneccion a Mysql en el phpmyadmin
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="blog"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM articles "
mycursor.execute(sql)
myresult = mycursor.fetchall()

#Conexion a mongodb 
#Indicarparametrosdel servidor
CLIENT = MongoClient("mongodb://localhost:27017") 
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)
    
DBS = CLIENT.get_database('Examen')  #Select the Schema 
db = DBS.MySql  #Select the Collection 

#Subir datos a MongoDB de los datos recopilados de MySQL

for row in myresult:
    doc={} 
    doc['_id']=row[0]
    doc['title'] =row[1]
    doc['body'] = row[2]
    doc['created_at']=row[3]
    doc['updated_at'] = row[4]
    doc['user_id'] =  row[5]
    doc['category_id'] = row[6]
    try:
        print(doc)
        db.insert_one(doc)
        print("guardado exitosamente")
    except Exception as e:    
        print("no se pudo grabar:" + str(e))



