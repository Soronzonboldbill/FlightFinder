""" 
    utils.py

    Purpose: simple script that connects to a MongoDB 
    Date   : 5/19/2023
    Author : Bill Soronzonbold  
"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# required for certificate verify failed error 
import certifi 
ca = certifi.where()

uri = 'mongodb+srv://bsoron01:Gs6ACvEwXohzFNq4@cluster0.6h4kape.mongodb.net/?retryWrites=true&w=majority'

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Code to get a cluster and print out information
try: 
    db = client['sample_airbnb']
    collection = db['listingsAndReviews'] 

    print(collection.find_one({
        "name" : "Ribeira Charming Duplex"
    }))

except Exception as e: 
    print(e) 

