import json

from sqlalchemy import Column, Integer, String, Boolean

from chalicelib.db import base


class Book(base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    read = Column(Boolean, default=False)

    def __repr__(self):
        return json.dumps({"id": self.id, "title": self.title,
                           "author": self.author, "read": self.read})
