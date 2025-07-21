# routes/product.py
from fastapi import APIRouter, Query
from models.product import Product
from db import product_collection
from bson import ObjectId
import re

router = APIRouter()

@router.post("/products", status_code=201)
def create_product(product: Product):
    result = product_collection.insert_one(product.dict())
    return {"_id": str(result.inserted_id)}

@router.get("/products", status_code=200)
def list_products(
    name: str = None,
    size: str = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}
    if size:
        query["sizes"] = size

    products = product_collection.find(query).skip(offset).limit(limit)
    result = []
    for product in products:
        product["_id"] = str(product["_id"])
        result.append(product)
    return result
