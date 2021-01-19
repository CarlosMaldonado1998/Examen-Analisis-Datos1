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

#Conexion a mongodb
CLIENT = MongoClient('mongodb://localhost:27017') #Indicarparametrosdel servidor
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

bd1 = CLIENT.Examen#SeleccionarSchema
db1 = bd1.Twitter#SeleccionarColeccion

#Recopilar los documenos de la base de couchDB y guardarlos de uno en uno en mongoDB
for id in db:
    if(db1.find_one({"_id" : db[id].id})):
        print("This id of the document already exist")
    else:
        db1.insert_one(db[id])
        