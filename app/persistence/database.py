from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from app.persistence.models import Base
from app.config import get_database_config

class Database:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            config = get_database_config()
            url = URL.create(
                drivername="postgresql",
                username=config.username,
                password=config.password,
                host=config.host,
                port=5432,
                database=config.name
            )
            engine = create_engine(url=url)
            Base.metadata.create_all(engine)
            cls.instance.db = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return cls.instance


def get_db():
    db = Database()
    try:
        yield db.instance.db()
    finally:
        db.instance.db().close()


