import requests
from pymongo import MongoClient

# Step 1: Get data from public API
api_url = "https://fakestoreapi.com/products"
response = requests.get(api_url)
product_data = response.json()

# Step 2: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Change if using MongoDB Atlas
db = client["store_db"]          # Database name
collection = db["products"]      # Collection name

# Optional: Clear previous data to avoid duplicates
collection.delete_many({})

# Step 3: Insert data into MongoDB
collection.insert_many(product_data)

print("✅ Product data successfully saved to MongoDB!")
