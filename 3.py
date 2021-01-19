from facebook_scraper import get_posts
from pymongo import MongoClient
import couchdb

#Conexion a mongodb 
#Indicarparametrosdel servidor
CLIENT = MongoClient("mongodb://localhost:27017") 
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)
    
DBS = CLIENT.get_database('Examen')  #Select the Schema 
db = DBS.Facebook  #Select the Collection 

#Leer los datos de facebook y mandarlos a mongoDB
i=1
for post in get_posts('Tecnosmartec', pages = 100):
    print(i)
    i=i+1
       
    id=post['post_id']
    doc={}
     
    doc['_id']=id
    
    mydate=post['time']
    
    try:
        doc['texto'] =post['text']
        doc['date'] =mydate.timestamp()
        doc['likes']=post['likes']
        doc['image'] = post['image'];
        doc['video'] =  post['video']; 
        doc['comments'] =post['comments']
        doc['shares'] =post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        db.insert_one(doc)
        print("guardado exitosamente")
    except Exception as e:    
        print("no se pudo grabar:" + str(e))