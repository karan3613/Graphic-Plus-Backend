from pymongo.mongo_client import MongoClient


uri = "Enter your MongoDb connect URL "

# Create a new client and connect to the server
client = MongoClient(uri)

db = client.GraphicApiDataBase

login_collection = db['login']
forgotPassword_collection = db['forgotPassword']
forgotId_collection = db['forgotId']
user_collection = db['user']
community_collection = db['community']
attendance_collection = db['attendance']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)