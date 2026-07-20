import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Database:
    def __init__(self, engine_url: str):
        """
        Initialize the database with a given engine URL.
        
        :param engine_url: The connection string for the database engine.
        """
        self.engine = sa.create_engine(engine_url)
        Base.metadata.bind = self.engine
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.SessionLocal = SessionLocal

    @classmethod
    def create_tables(cls, engine_url: str):
        """
        Create all tables in the database.
        
        :param engine_url: The connection string for the database engine.
        """
        with cls(engine_url) as db:
            Base.metadata.create_all(bind=db.engine)

    @classmethod
    def get_db(cls, engine_url: str) -> 'Generator[Session, None, None]':
        """
        Get a database session generator.
        
        :param engine_url: The connection string for the database engine.
        :return: A generator yielding a database session.
        """
        db = None
        try:
            with cls(engine_url) as db:
                yield db
        finally:
            if db:
                db.close()

    def __enter__(self):
        return self.SessionLocal()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Example usage of the Database class
if __name__ == "__main__":
    engine_url = "sqlite:///example.db"
    db = Database(engine_url)
    db.create_tables(engine_url)
