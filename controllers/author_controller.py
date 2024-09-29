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
        return {"error": f"Author with id {author_id} not found!"}, 404 # Bad Request


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
        return {"message": f"Author {author.first_name} {author.last_name} successfully added to the book {book.title}!"}, 200 # Created successfully
    # Else
    else:
        # Return error
        return {"error": f"A book with id {book_id} does not exist!"}, 404 # Bad Request

# DELETE - remove an author from a specific book | /books/<book_id>/authors/
@author_bp.route("/books/<int:book_id>/authors/", methods=["DELETE"])
@jwt_required()
def delete_author(book_id):
    # Fetch the book with the id=book_id
    book_stmt = db.select(Book).filter_by(id=book_id)
    book = db.session.scalar(book_stmt)

    # Check if the book exists
    if book:
        # Check if the book has an associated author
        if book.author_id is not None:
            # Unassign the author
            book.author_id = None  # Remove the association with the author
            
            db.session.commit()
            
            return {"message": f"Author has been removed from the book '{book.title}'!"}, 200  # Request Successful
        else:
            return {"error": f"The book '{book.title}' has no associated author."}, 400  # Bad Request
    else:
        # Return error if the book doesn't exist
        return {"error": f"A book with id {book_id} does not exist!"}, 404  # Not Found


# PUT/PATCH - update a specific author associated with a book | /books/<book_id>/authors/<author_id>
@author_bp.route("/books/<int:book_id>/authors/<int:author_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_author(book_id, author_id):
    # Get the data from the body of the request
    body_data = request.get_json()

    # Fetch the author from the database
    author_stmt = db.select(Author).filter_by(id=author_id)
    author = db.session.scalar(author_stmt)

    # Fetch the book with the id=book_id
    book_stmt = db.select(Book).filter_by(id=book_id)
    book = db.session.scalar(book_stmt)

    # Check if both the author and book exist
    if author and book:
        # Check if the author is associated with the book
        if book.author_id == author.id:
            # Update the author fields as required
            author.first_name = body_data.get("first_name") or author.first_name
            author.last_name = body_data.get("last_name") or author.last_name

            # Commit to the db
            db.session.commit()

            # Return acknowledgment
            return author_schema.dump(author), 200  # Updated Successfully
        else:
            return {"error": f"The author is not associated with the book '{book.title}'."}, 400  # Bad Request
    else:
        # Return an error message
        if not author:
            return {"error": f"Author with id {author_id} not found!"}, 404  # Not Found
        if not book:
            return {"error": f"Book with id {book_id} not found!"}, 404  # Not Found
