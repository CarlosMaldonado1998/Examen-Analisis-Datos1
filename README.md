# Examen-Analisis-Datos1
En la carpeta se encuentran scripts de phyton que muestran diversas funcionalidades para la gestion de datos en bases como couchDb y mongoDB

- 1 Twitter to couchDB

El script posee las credenciales de la API para el acceso a la información, de esta se recopilan los datos en el sector de quito. Y luego se hace una conección a couchDB y se procede a subir los datos. 

- 2 WebScraping to mongoDB

El script recopila los datos de una página web de venta de productos electronicos, los ordena en un dataFrame para posteriormente subirlos a la base de datos MongoDB.

- 3 Facebook to mongoDB

El script recopila los datos de una página de Facebook donde se recopilan los posts publicados en la misma, se generan documentos por id y estos se empiezan a subir a la base de datos mongoDB

- 4 MySql to mongoDB

El scritp con el uso de mysql.connector nos conectamos a una base creada y recopilamos información mediante una consulta SQL a determinada tabla, posteriormente se organiza esta informacion y es subida a la base de datos de mongoDB. 

- 5 CouchDB to MongoDb

El scritp realiza las conecciones a las dos bases de datos donde se itera los datos de couchdb   y estos son enviados a MongoDB

- 6 MongoDb to couchDB

El scritp realiza las conecciones a las dos bases de datos donde se iteran las coleccioens de mongoDb y se envia cada documento a couchDB

- 7 CouchDb to MongoDb Atlas 

El scritp realiza las conecciones a las dos bases de datos donde se itera los datos de couchdb   y estos son enviados a MongoDB Atlas 

- 8 MongoDb to MongoDb Atlas 

El scritp realiza las conecciones a las dos bases de datos donde se iteran las coleccioens de mongoDb y se envia cada colección con sus respectivos documentos a la base de mongodb Atlas 

-9 MongoDb to Atlas 

El escript realiza la conección a mongoDb Atlas recoge los documentos de una colección y luego se procede convertirlos en arrays y para hacer un dataframe y poder convertir este en archivo csv.
