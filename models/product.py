from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    name: str
    description: str
    price: float
    sizes: List[str]
