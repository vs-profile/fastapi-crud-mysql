from fastapi import FastAPI, HTTPException, Query
from model.customers import customers, customers_update
from config.database import create_db_and_tables
from contextlib import asynccontextmanager
from add_customers import add_data
from query_customers import all_customers, customers_by_id
from update_customers import update_customer
from delete_cutomers import delete_customer

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables()
    yield


app=FastAPI(lifespan=lifespan)


@app.get("/customers/", response_model=list[customers])
def customers_all(offset: int=0, limit: int = Query(default=100, le=100)):
    result = all_customers(offset, limit)
    return result



@app.post("/customers/",response_model=customers)
def add_customer(customer: customers):
    result = add_data(customer)
    return result

@app.get("/customers/{id}", response_model=customers)
def get_by_id(id: int):
    result = customers_by_id(id)
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="customer not found")
    return result

@app.patch("/customers/{cust_id}", response_model=customers)
def update(cust_id: int, customer: customers_update):
    result = update_customer(cust_id, customer)
    if not result:
        raise HTTPException(status_code=404, detail="customer not found")
    return result

@app.delete("/customers/{cust_id}")
def delete(cust_id: int):
    result = delete_customer(cust_id)
    if result == 0:
        raise HTTPException(status_code=404, detail="customer not found")
    return {"ok": True}