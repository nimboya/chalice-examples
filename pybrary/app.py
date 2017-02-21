from chalice import Chalice

from chalicelib.db import db, base
from chalicelib.methods.book import (get_all_books, create_book,
                                     get_book_by_id, update_book_by_id,
                                     delete_book_by_id)


app = Chalice(app_name='do_not_user_this_for_presentation')
app.debug = True


base.metadata.create_all(db)


@app.route('/books', methods=['GET', 'POST'])
def books():
    request = app.current_request

    if request.method == 'GET':
        return get_all_books()
    elif request.method == 'POST':
        return create_book(request)


@app.route('/books/{id}', methods=['GET', 'PUT', 'DELETE'])
def books_id(id):
    request = app.current_request

    if request.method == 'GET':
        return get_book_by_id(id)
    elif request.method == 'PUT':
        return update_book_by_id(id, request)
    elif request.method == 'DELETE':
        return delete_book_by_id(id)
