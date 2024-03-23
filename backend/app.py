from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb+srv://ataduri7:Midnight@cluster0.lv7rogd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['MainDB']
collection = db['Pictures']

# Define endpoint to serve data
@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))  # Exclude _id field from the response
    return jsonify({'data': data})

# Define route for root URL
@app.route('/', methods=['GET'])
def home():
    return "Welcome to my Flask app! Visit /data to access the data."

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)


