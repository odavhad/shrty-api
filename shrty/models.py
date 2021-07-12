from enum import unique
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

from .database import Base


class URLModel(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_tag = Column(String, unique=True, nullable=False)
    target_url = Column(String, nullable=False)
    visit_count = Column(Integer, default=0)
    public = Column(Boolean, default=False)
