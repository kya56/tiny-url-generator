from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, BigInteger, String, TIMESTAMP, func

class Base(DeclarativeBase):
    pass

class Uri(Base):
    __tablename__ = "uri"

    id = Column(BigInteger, primary_key=True, nullable=False)
    long_uri = Column(String, nullable=False)
    short_uri = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
