from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["store_db"]
collection = db["products"]

# Load data into a DataFrame
data = list(collection.find())
df = pd.DataFrame(data)

# Convert the _id field to string if needed
df["_id"] = df["_id"].astype(str)

# Export to CSV in E:\ drive
csv_file_path = r"C:\products.csv"  # Save directly in E:\ drive
df.to_csv(csv_file_path, index=False)

print(f"Data exported to {csv_file_path} successfully!")