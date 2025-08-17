#while working on this project this code was first pasted in push_data.py with username
#  and password to check whether connection is getting established to the mongo db database or not. 
# now since we have verified that connection is getting established i have pasted this code here
#  so that you can also enter username or password and check whether this is working or not
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://AryanRoy:Aryan123@cluster0.hcq9pco.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)