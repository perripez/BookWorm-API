from datetime import date

from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from init import db
from models.book import Book, book_schema, books_schema
from controllers.review_controller import reviews_bp

books_bp = Blueprint("books", __name__, url_prefix="/books")
books_bp.register_blueprint(reviews_bp)

# GET - fetch all books in db | /books
@books_bp.route("/")
def get_all_books():
    stmt = db.select(Book) # SELECT * FROM books
    books = db.session.scalars(stmt)
    return jsonify(books_schema.dump(books))

# GET BOOK ID - fetch a specific book in db | /books/<id>
@books_bp.route("/<int:book_id>")
def get_book(book_id):
    stmt = db.select(Book).filter_by(id=book_id)
    # SELECT * FROM books WHERE id = 'book_id value';
    book = db.session.scalar(stmt)
    if book:
        return book_schema.dump(book)
    else:
        return {"error": f"Book with id {book_id} not found!"}, 404 # Bad Request

# POST - create a new book entry | /books
@books_bp.route("/", methods=["POST"])
@jwt_required()
def create_book():
    # Get the data from the body of the request
    body_data = request.get_json()
    # Create an instance of the book model
    book = Book(
        title = body_data.get("title"),
        publication_year = body_data.get("publication_year"),
        date = date.today(),
        user_id = get_jwt_identity()
    )
    # Add + commit to the database
    db.session.add(book)
    db.session.commit()
    # Return acknowledgement
    return book_schema.dump(book), 201 # Created

# DELETE - delete a specific book from db | /books/<id>
@books_bp.route("/<int:book_id>", methods=["DELETE"])
@jwt_required()
def delete_book(book_id):
    # Fetch the book from the db
    stmt = db.select(Book).filter_by(id=book_id)
    # ^ SELECT * FROM books WHERE id = 'book_id value';
    book = db.session.scalar(stmt)
    # If the book exists
    if book:
        # Delete the book
        db.session.delete(book)
        db.session.commit()
        return {"message": f"Book with id {book_id} has been deleted"}, 200 # Request successful
    # Else
    else:
        # Return error
        return{"error": f"Book with id {book_id} does not exist!"}, 404 # Bad Request

# PUT, PATCH - edit a specific book entry | /books/<id>
@books_bp.route("/<int:book_id>", methods=["PUT","PATCH"])
@jwt_required()
def edit_book(book_id):
    # Get the data from the body of the request
    body_data = request.get_json()
    # Fetch the book from the db
    stmt = db.select(Book).filter_by(id=book_id)
    # ^ SELECT * FROM books WHERE id = 'book_id value';
    book = db.session.scalar(stmt)
    # If the book exists
    if book:
        # Update the book fields as required
        book.title = body_data.get("title") or book.title
        book.publication_year = body_data.get("publication_year") or book.publication_year
        # Commit to the db
        db.session.commit()
        # Return acknowledgement
        return book_schema.dump(book), 200 # Updated Successfully
    # Else
    else:
        # Return an error message
        return {"error": f"Book with id {book_id} not found!"}, 400 # Bad Request
