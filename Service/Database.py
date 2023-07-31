
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


'''
mongo db pass: 

test : oumUKp6wiGI67ed7
admin: admin

'''

def get_connect_db(username,password):

    uri = f"mongodb+srv://{username}:{password}@cluster-stockmarket.ysmczsq.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client


def get_database_create(username,password,databasename, collectionname,data):
    uri = f"mongodb+srv://{username}:{password}@cluster-stockmarket.ysmczsq.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = get_connect_db(username,password)[f"{databasename}"]
    collection = db[f"{collectionname}"]
    collection.insert_one(data)
def get_database_delete():
    print("Databaseden silindi")
    

