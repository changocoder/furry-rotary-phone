from pydantic import BaseModel


class Customer(BaseModel):
    name: str
    last_name: str
    identifier: str
    sex: str
