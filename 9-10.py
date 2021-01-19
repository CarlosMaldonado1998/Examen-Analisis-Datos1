import json
import pymongo
import pandas as pd


#Conexion a mongodb Atlas
SERVER = pymongo.MongoClient("mongodb+srv://Videogames:videogames@cluster0.60gzs.mongodb.net/Twiter?retryWrites=true&w=majority")

try:
    SERVER.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)
    
DBSA = SERVER.get_database('Examen')
dbsCollection = DBSA.WebScraping
    
my_database = dbsCollection.find()

#Iterar en los documentos de la colección, añadiendolos a un vector para poserior añadir al dataframe

values=[]
for document in my_database:
    values.append(document)
    pd.DataFrame([values]).to_csv('9.csv', index=False)