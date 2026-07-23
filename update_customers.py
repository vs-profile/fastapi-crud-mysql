from sqlmodel import Session, select
from config.database import engine
from model.customers import customers, customers_update


def update_customer(customer_id: int, cust: customers_update):
    with Session(engine) as session:
        db_customer = session.get(customers, customer_id)
        if not db_customer:
            return None
        else:
            customer_data = cust.model_dump(exclude_unset=True)
            db_customer.sqlmodel_update(customer_data)
            session.add(db_customer)
            session.commit()
            session.refresh(db_customer)
            return db_customer
