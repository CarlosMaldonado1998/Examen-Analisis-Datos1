import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
###API ########################
ckey = "mrBmNMHFbxT5Ch55FogGSMdXH"
csecret = "CI9MgalOzxZK9F7Ih10xVBBy9iLPM7D3B3rhW9EWZKrVwD9WOM"
atoken = "2332150468-9XICKNCjbNXjWhtvKCAwuLVB8y5SYJ7zgCZZKhb"
asecret = "pOyhybuqnNVNS2ghs62VeNVuIEzMVPfT2Cj5zOxpRkrPF"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:sistemas@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('examen1')
except:
    db = server['examen']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-78.619545,-0.408764,-78.259892,-0.047208])  
twitterStream.filter(track=['presidente'])