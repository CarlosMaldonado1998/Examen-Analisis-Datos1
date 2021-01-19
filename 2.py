import pandas as pd
from bs4 import BeautifulSoup
import requests 
from pymongo import MongoClient

def find_2nd(string, substring):
    return string.find(substring, string.find(substring)+1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))
response = requests.get('https://www.tecnosmart.com.ec/shop/category/hardware-o-componentes-de-pc-procesadores-12')
soup = BeautifulSoup(response.content, "lxml")

Name = []
ID =[]
Price= []
Description = []


product_name = soup.find_all("a", class_="product_name_ec")
product_ID = soup.find_all("input" , {"name" : "product_id"} )
product_price = soup.find_all(itemprop= "price")
product_description = soup.find_all( itemprop = "description")


for element in product_name:
    element = str(element)
    limpio = str(element[find_1st(element, '>')+1:find_2nd(element, '<')], )
    Name.append(limpio.strip())
for element in product_ID:
    element = str(element)
    limpio = str(element[find_1st(element, 'value="')+7:find_2nd(element, '"/')-2], )
    ID.append(limpio.strip())
for element in product_price:
    element = str(element)
    limpio = str(element[find_1st(element, '>')+1:find_2nd(element, '<')], )
    Price.append(limpio.strip())
for element in product_description:
    element = str(element)
    limpio = str(element[find_1st(element, '>')+1:find_2nd(element, '<')], )
    Description.append(limpio.strip())

#Generar un dataFrame 
dfDs = pd.DataFrame({ 'Product_Name': Name, 'Product_ID': ID , 'Price': Price,  'Description' : Description })
dfDs


#Conexion a mongodb 
#Indicarparametrosdel servidor
CLIENT = MongoClient("mongodb://localhost:27017") 
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)
    
DBS = CLIENT.get_database('Examen')  #Select the Schema 
db = DBS.WebScraping  #Select the Collection 


#Recorrer el DataFrame de pandas
#Guardar los datos en mongoDB
for i in dfDs.index:
    document = {
        "_id" : dfDs["Product_ID"][i],
        "Product Name" : dfDs["Product_Name"][i],
        "Price" : dfDs["Price"][i],
        "Description" : dfDs["Description"][i],
    }
    try:
        db.insert_one(document)
        print("guardado exitosamente")
    except Exception as e:    
        print("no se pudo grabar:" + str(e))
