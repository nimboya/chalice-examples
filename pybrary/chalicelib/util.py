from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from chalicelib.db import db


session = sessionmaker(bind=db)()


@contextmanager
def get_session():
    yield session
