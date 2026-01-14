import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:123Olga456@localhost:5432/postgres"


@pytest.fixture(scope="session")
def engine():
    return create_engine(DATABASE_URL)


@pytest.fixture(scope="function")
def db_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.rollback() 
    session.close()
