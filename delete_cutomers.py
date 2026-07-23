from sqlmodel import Session
from config.database import engine
from model.customers import customers


def delete_customer(customer_id: int):
    with Session(engine) as session:
        db_customer = session.get(customers, customer_id)
        if not db_customer:
            return 0
        else:
            session.delete(db_customer)
            session.commit()
            return 1
