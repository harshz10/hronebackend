# main.py
from fastapi import FastAPI
from routes import product, order

app = FastAPI(
       title="HROne API",
    docs_url="/docs",       #
    redoc_url="/redoc",     
    openapi_url="/openapi.json"
)

# Include both routes
app.include_router(product.router)
app.include_router(order.router)

@app.get("/")
def root():
    return {"message": " HROne Backend Task  by Harsh Nagar"}
