# main.py
from fastapi import FastAPI
from routes import product, order

app = FastAPI()

# Include both routes
app.include_router(product.router)
app.include_router(order.router)

@app.get("/")
def root():
    return {"message": " HROne Backend Task  by Harsh Nagar"}
