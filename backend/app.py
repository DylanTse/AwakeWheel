from flask import Flask
import requests
import json
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

m_api_key = os.getenv("API_KEY")
m_url = os.getenv("URL")


app = Flask(__name__)

# MongoDB connection

@app.route('/')
def get_data():
    # Example: Querying data from the collection
    return {"message": "Hello, World!"}

@app.route('/get_photos')
def get_photos():
    url = m_url + "/action/find"
    payload = json.dumps({
        "collection": "Wheel",
        "database": "Awake",
        "dataSource": "Cluster0",
        "projection": {
            "base64Image": 1,
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': m_api_key,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
