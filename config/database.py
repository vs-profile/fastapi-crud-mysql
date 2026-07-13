from sqlmodel import SQLModel, create_engine
from urllib.parse import quote_plus

# MySQL connection string
engine = create_engine(
    f"mysql+pymysql://root:"
    f"{quote_plus('root')}"
    f"@localhost:3306/employee"
)

# Function to create database tables from SQLModel classes
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)