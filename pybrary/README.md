Pybrary
=======

Pybrary is a minimal API that was created by Jesse Horne during the Pyowa presentation on February 7, 2017. It is meant to be a CRUD for books. It connects to an in-memory sqlite database, and allows the user of the API to create, get, update, and delete book listings.

### Running Pybrary
```
cd pybrary/
mkvirtualenv pybrary
pip install -r requirements.txt
chalice local
```

### Create Book (POST "/books")
JSON
```
{
  "author": "Peter Kropotkin",
  "title": "The Conquest of Bread",
  "read": false
}
```

### Get All Books (GET "/books")
### Get Book by ID (GET "/books/1")

### Update Book (PUT "/books/1")
JSON
```
{
  "author": "Peter Kropotkin",
  "title": "The Conquest of Bread",
  "read": true
}
```

### Delete Book by ID (DELETE "/books/1")
