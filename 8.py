from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import dns
import json

#Conexion a mongodb

CLIENT = pymongo.MongoClient('mongodb://localhost:27017')#Indicarparametrosdel servidor

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

#SeleccionarSchema
DBS = ['Examen']


#Conexion a mongodb Atlas
SERVER = pymongo.MongoClient("mongodb+srv://Videogames:videogames@cluster0.60gzs.mongodb.net/Twiter?retryWrites=true&w=majority")

try:
    SERVER.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)
    
DBSA = SERVER.get_database('Examen')


for db in DBS:
       if db in ('Examen'):  
        cols = CLIENT[db].list_collection_names() 
        for col in cols:
            dbsCollectionA = DBSA[col]
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    documents = json.loads(json_util.dumps(x))
                    dbsCollectionA.insert_one(documents)
                    print("SAVE")
                    print(documents)
                except:
                    print("This document already exist")