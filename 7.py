import couchdb
import requests
from pymongo import MongoClient

#Conexion a couchDb
URL = 'http://admin:sistemas@localhost:5984'
try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e
server=couchdb.Server(URL)
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
db = server['examen1']

#Conexion a mongodb Atlas
#Indicarparametrosdel servidor
CLIENT = MongoClient("mongodb+srv://Videogames:videogames@cluster0.60gzs.mongodb.net/Twiter?retryWrites=true&w=majority") 
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)
    
DBS = CLIENT.get_database('Examen')  #Select the Schema 
db1 = DBS.couchdb  #Select the Collection 
 
    
#Recopilar los documenos de la base de couchDB y guardarlos de uno en uno en mongoDB
for id in db:
    try:
        if(db1.find_one({"_id" : db[id].id})):
            print("This document already exist")
        else:
            db1.insert_one(db[id])
            print("SAVE")
            print(db1.find_one({"_id" : db[id].id}))
    except:
        print("Error al guardar los datos")