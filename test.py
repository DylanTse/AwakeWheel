import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

m_api_key = os.getenv("API_KEY")
print(m_api_key + "here")
url = "https://us-east-2.aws.data.mongodb-api.com/app/data-kuvdq/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "Wheel",
    "database": "Awake",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': m_api_key,
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)