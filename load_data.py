from pymongo import MongoClient
import pandas as pd

MONGO_URI = "mongodb+srv://nikrajsun_db_user:Mongo,123@cluster0.dza0j5j.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["ev_db"]
collection = db["vehicles"]

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
df = df.fillna("")

records = df.to_dict(orient="records")

batch_size = 1000
for i in range(0, len(records), batch_size):
    batch = records[i:i+batch_size]
    collection.insert_many(batch)

print("DONE")