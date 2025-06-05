from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["store_db"]
collection = db["products"]

# Load and convert to DataFrame
data = list(collection.find())
df = pd.DataFrame(data)

# Remove MongoDB’s internal ID if needed
if '_id' in df.columns:
    df.drop(columns=['_id'], inplace=True)

# Export to CSV
df.to_csv("products.csv", index=False)
print("✅ Exported data to products.csv")
