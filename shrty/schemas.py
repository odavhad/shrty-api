from pydantic import BaseModel
from typing import Optional


class UserAuth(BaseModel):
    username: str
    password: str


class URLSchema(BaseModel):
    short_tag: str
    target_url: str
    public: Optional[bool] = False


class URLSchemaCreate(URLSchema):
    visit_count: Optional[int] = 0


class URLSchemaModify(URLSchema):
    visit_count: Optional[int]


class URLDatabase(URLSchema):
    id: int

    class Config:
        orm_mode = True

