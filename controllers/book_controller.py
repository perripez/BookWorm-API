from datetime import datetime, date

from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow import ValidationError

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
    
    # Validate incoming data against the schema
    try:
        validated_data = book_schema.load(body_data)  # Validate without the instance

        # Validate publication year directly
        publication_year = validated_data.get("publication_year")
        current_year = datetime.now().year
        if publication_year < 1450 or publication_year > current_year:
            return {"error": f"Publication year must be between 1450 and {current_year}!"}, 400  # Bad Request

        # Create an instance of the book model
        new_book = Book(
            title=validated_data.get("title"),
            publication_year=publication_year,
            date=date.today(),
            user_id=get_jwt_identity()
        )

        # Add + commit to the database
        db.session.add(new_book)
        db.session.commit()

        # Return acknowledgement
        return book_schema.dump(new_book), 201  # Created

    except ValidationError as err:
        return {"error": err.messages}, 400  # Bad Request with error messages

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
    # Fetch the book from the database
    stmt = db.select(Book).filter_by(id=book_id)
    book = db.session.scalar(stmt)

    # If the book exists
    if book:
        # Get the data from the body of the request
        body_data = request.get_json()
        
        # Validate the incoming data against the schema without the instance
        try:
            updated_data = book_schema.load(body_data)  # Validate without the instance

            # Validate publication year directly
            publication_year = updated_data.get("publication_year")
            if publication_year is not None:
                current_year = datetime.now().year
                if publication_year < 1450 or publication_year > current_year:
                    return {"error": f"Publication year must be between 1450 and {current_year}!"}, 400  # Bad Request
            
            # Update the book fields if provided in the request
            book.title = updated_data.get("title", book.title)
            book.publication_year = publication_year or book.publication_year

            # Commit to the db
            db.session.commit()

            # Return acknowledgement
            return book_schema.dump(book), 200  # Updated successfully

        except ValidationError as err:
            return {"error": err.messages}, 400  # Bad Request with error messages

    # Else return an error message
    return {"error": f"Book with id {book_id} not found!"}, 404  # Not Found