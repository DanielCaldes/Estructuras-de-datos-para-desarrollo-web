from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, TypeVar
from structures.linked_list import LinkedList
from structures.bst import BST
import os
import sys
import json

# COMANDO: uvicorn "main:app" --reload

app = FastAPI()

project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_root)

#Paths to store data
PRODUCTS_PATH = os.path.join("data","products.json")
ORDERS_PATH = os.path.join("data","orders.json")

class State:
    last_product_id = 0
    last_order_data_id = 0

class Product(BaseModel):
    id: Optional[int] = None
    product_name :str
    price : float

class Order(BaseModel):
    products : List[Product]

class OrderData(BaseModel):
    id: Optional[int] = None
    products: Dict[int, int]

def compare_by_id(product1, product2):
    if product1.id < product2.id:
        return -1
    elif product1.id > product2.id:
        return 1
    else:
        return 0

def compare_by_search_key(id, product2):
    if id < product2.id:
        return -1
    elif id > product2.id:
        return 1
    else:
        return 0


# {"product_name":"Patatas", "price":2}
# {"products":{"1":2,"2":1}}

#Create structures
orders_linkedList = LinkedList()
products_bst = BST(compare_by_id, compare_by_search_key)
state = State()


T = TypeVar('T', bound=BaseModel)

def write_to_json(models: List[T], path: str):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump([model.model_dump() for model in models], file, indent=4, ensure_ascii=False)
    return

def read_from_json(path: str, model_class : T) -> List[T]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data_dict = json.load(file)
            return [model_class(**data) for data in data_dict]
    except FileNotFoundError:
        print(f"El archivo {path} no existe. Retornando lista vacía.")
        return []
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {path}. Verifique el formato del archivo.")
        return []

#Load products
products = read_from_json(PRODUCTS_PATH, Product)
last_product_id = 0
for product in products:
    if product.id > last_product_id:
        last_product_id = product.id
    products_bst.insert(product)
state.last_product_id = last_product_id
#Load orders
orders = read_from_json(ORDERS_PATH, OrderData)
last_order_id = 0
for order in orders:
    if order.id > last_order_id:
        last_order_id = order.id
    orders_linkedList.insert(order)
state.last_order_data_id = last_order_id


#a) Create product
@app.post("/api/products")
def create_product(product : Product):
    state.last_product_id += 1
    product.id = state.last_product_id
    products_bst.insert(product)
    write_to_json(products_bst.inorder(), PRODUCTS_PATH)
    return {"message" : f"Product created with id : {product.id}"}

#b) Show product by id
@app.get("/api/products/{id}")
def product_info(id : int):
    product = products_bst.search(id)
    if product:
        product_info = {"product name": product.value.product_name,"product price": product.value.price}
        return product_info
    else:
        raise HTTPException(status_code=500, detail="No product with that id")

#c) Create order
@app.post("/api/orders")
def create_order(order_data : OrderData):
    state.last_order_data_id += 1
    order_data.id = state.last_order_data_id
    orders_linkedList.insert(order_data)
    write_to_json(orders_linkedList.list_items(), ORDERS_PATH)
    return {"message" : f"Order created with id : {order_data.id}"}

def products_in_order(order):
    if order:
        products_ids = order.products
        products = []
        total_price = 0
        for product_id, quantity in products_ids.items():
            product_node = products_bst.search(product_id)
            if product_node:
                product = product_node.value
                products.append({
                    "product_name": product.product_name,
                    "product_price": product.price,
                    "quantity": quantity,
                    "total_price": product.price * quantity
                })
                total_price += product.price * quantity
        return{
            "products":products,
            "total_price":total_price
        }
    return {}

#d) Find order by id
@app.get("/api/orders/{id}")
def order_info(id : int):
    order = orders_linkedList.find(lambda order: order.id == id)
    if order:
        products = products_in_order(order)
        return products
    else:
        raise HTTPException(status_code=500, detail=f"No order with that id {id}")
    
#e) update order
@app.put("/api/orders/{id}")
def update_order(id : int, order_data : OrderData):
    order_updated = orders_linkedList.find(lambda order: order.id == id)
    if order_updated:
        order_updated.products = order_data.products
        write_to_json(orders_linkedList.list_items(), ORDERS_PATH)
        return {"message" : "Order updated!"}
    else:
        raise HTTPException(status_code=500, detail="No order with that id")

#f) delete order
@app.delete("/api/orders/{id}")
def delete_order(id : int):
    order_deleted = orders_linkedList.delete(lambda order: order.id == id)
    if order_deleted:
        write_to_json(orders_linkedList.list_items(), ORDERS_PATH)
        return{"message" : "Order deleted!"}
    else:
        raise HTTPException(status_code=500, detail=f"No order with that id {id}")

#g) list all orders
@app.get("/api/orders")
def list_orders():
    order_dict = {}
    for order in orders_linkedList.list_items():
        order_dict[f"order_{order.id}"] = products_in_order(order)
    return order_dict
