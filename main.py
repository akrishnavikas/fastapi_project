from fastapi import FastAPI
from models import Product


app = FastAPI()

products = [Product(id=1, name="Laptop", description="A powerful laptop", price=999.99, quantity=10),
            Product(id=2, name="Smartphone", description="A sleek smartphone", price=499.99, quantity=20),
            Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=15),
            Product(id=4, name="Smartwatch", description="A stylish smartwatch", price=299.99, quantity=5),
            Product(id=5, name="Tablet", description="A versatile tablet", price=399.99, quantity=8)]

@app.get("/")
def greet():
    return {"message": "Hello, World!"}

@app.get("/product")
def get_products():
    return products


@app.get("/product/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return products

@app.put("/product")
def update_product(id: int,product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Added Successfully"
        
    return "No prodcut Found"


@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return "No product Found"