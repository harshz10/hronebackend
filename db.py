from dotenv import load_dotenv  
import os                      
from pymongo import MongoClient  


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.hrodb
product_collection = db.products
order_collection = db.orders