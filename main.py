from itertools import count

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Product
import database_models
from database import session, engine


app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

products = [Product(id=1, name="Laptop", description="A powerful laptop", price=999.99, quantity=10),
            Product(id=2, name="Smartphone", description="A sleek smartphone", price=499.99, quantity=20),
            Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=15),
            Product(id=4, name="Smartwatch", description="A stylish smartwatch", price=299.99, quantity=5),
            Product(id=5, name="Tablet", description="A versatile tablet", price=399.99, quantity=8),
            Product(id=6, name="Camera", description="A high-resolution camera", price=899.99, quantity=12),
            Product(id=7, name="Printer", description="A fast printer", price=149.99, quantity=7),
            Product(id=8, name="Monitor", description="A 4K monitor", price=299.99, quantity=6),
            Product(id=9, name="Keyboard", description="A mechanical keyboard", price=89.99, quantity=25)]

def init_db():
    db = session()
    count = db.query(database_models.Product).count()
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
    db.commit()
    db.close()


init_db()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def greet():
    return {"message": "Hello, World!"}

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()


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