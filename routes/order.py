from fastapi import APIRouter
from models.order import Order
from db import order_collection
from bson import ObjectId

router = APIRouter()

@router.post("/orders", status_code=201)
def create_order(order: Order):
    result = order_collection.insert_one(order.dict())
    return {"_id": str(result.inserted_id)}

@router.get("/orders/{user_id}", status_code=200)
def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    orders = order_collection.find({"user_id": user_id}).skip(offset).limit(limit)
    result = []
    for order in orders:
        order["_id"] = str(order["_id"])
        result.append(order)
    return result
