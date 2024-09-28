from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from init import db
from models.author import Author, author_schema, authors_schema
from models.book import Book, book_schema, books_schema

author_bp = Blueprint("authors", __name__)

# GET - fetch all authors | /authors
@author_bp.route("/authors")
def get_all_authors():
    stmt = db.select(Author) # SELECT * FROM authors
    authors =db.session.scalars(stmt)
    return authors_schema.dump(authors)

# GET - fetch a specific author in db | /authors/author_id
@author_bp.route("/authors/<int:author_id>")
def get_author(author_id):
    stmt = db.select(Author).filter_by(id=author_id)
    # SELECT * FROM authors WHERE id = 'author_id value';
    author = db.session.scalar(stmt)
    if author:
        return author_schema.dump(author)
    else:
        return {"error": f"Author with id {author_id} not found!"}


# POST - create a new author entry | /book_id/authors
@author_bp.route("/books/<int:book_id>/authors/", methods=["POST"])
@jwt_required()
def create_author(book_id):
    # Get the data from the body of the request
    body_data = request.get_json()
    # Fetch the book with the id=book_id
    stmt = db.select(Book).filter_by(id=book_id)
    # SELECT * FROM books WHERE id = 'book_id value';
    book = db.session.scalar(stmt)
    # if the book exists
    if book:
        # Create instance of author model
        author = Author(
            first_name = body_data.get("first_name"),
            last_name = body_data.get("last_name")
        )

        # Commit session to db
        db.session.add(author)
        db.session.commit()
        
        book.author_id = author.id
        db.session.commit()

        # return acknowledgement
        return {"message": f"Author {author.first_name} {author.last_name} successfully added to the book {book.title}!"}
    # Else
    else:
        # Return error
        return {"error": f"A book with id {book_id} does not exist!"}, 404 # Bad Request
