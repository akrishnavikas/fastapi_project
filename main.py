from fastapi import FastAPI
from models import Product


app = FastAPI()

products = [Product(id=1, name="Laptop", description="A powerful laptop", price=999.99, quantity=10),
            Product(id=2, name="Smartphone", description="A sleek smartphone", price=499.99, quantity=20)]

@app.get("/")
def greet():
    return {"message": "Hello, World!"}

@app.get("/products")
def get_products():
    return products