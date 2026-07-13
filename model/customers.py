from typing import Optional
from sqlmodel import Field, SQLModel


class customers(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str
    mobile: Optional[int] = None    

class customers_update(SQLModel):
    email: str
    mobile: Optional [int] = None 