import json

from chalice import NotFoundError, BadRequestError

from chalicelib.models.book import Book
from chalicelib.util import get_session


def create_book(request):
    # explain that this is just a simple catch-all
    try:
        title = request.json_body['title']
        author = request.json_body['author']
        read = request.json_body['read']

        with get_session() as session:
            new_book = Book(title=title, author=author, read=read)

            session.add(new_book)
            session.commit()

            return
    except Exception as e:
        raise BadRequestError(e)


def get_all_books():
    with get_session() as session:
        books = session.query(Book).all()

        return [json.loads(str(b)) for b in books]


def get_book_by_id(id):
    with get_session() as session:
        book = session.query(Book).filter_by(id=id).first()

        if not book:
            raise NotFoundError("That book doesn't exist.")

        return json.loads(str(book))


def update_book_by_id(id, request):
    with get_session() as session:
        existing_book = session.query(Book).filter_by(id=id).first()

        if not existing_book:
            raise NotFoundError("That book doesn't exist.")

        try:
            existing_book.title = request.json_body['title']
            existing_book.author = request.json_body['author']
            existing_book.read = request.json_body['read']

            session.commit()
        except Exception as e:
            raise BadRequestError(e)


def delete_book_by_id(id):
    with get_session() as session:
        book = session.query(Book).filter_by(id=id).first()

        if not book:
            raise NotFoundError("That book doesn't exist.")

        session.delete(book)

        session.commit()
