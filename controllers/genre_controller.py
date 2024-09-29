from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from init import db
from models.genre import Genre, genre_schema, genres_schema
from models.book import Book, book_schema, books_schema

genre_bp = Blueprint("genre", __name__)

# GET - fetch all genres | /genres
@genre_bp.route("/genres")
def get_all_genres():
    stmt = db.select(Genre) # SELECT * FROM genres
    genres = db.session.scalars(stmt)
    return genres_schema.dump(genres)

# GET - fetch a specific genre in db | /genre/genre_id
@genre_bp.route("/genres/<int:genre_id>")
def get_genre(genre_id):
    stmt = db.select(Genre).filter_by(id=genre_id)
    # SELECT * FROM genres WHERE id = 'genre_id value';
    genre = db.session.scalar(stmt)
    if genre:
        return genre_schema.dump(genre)
    else:
        return {"error": f"Genre with id {genre_id} not found!"}, 404 # Bad Request

# POST - create a new genre entry | /book_id/genres
ALLOWED_GENRES = {"Self help", "Autobiography", "Fiction", "Health", "Childrens"}
@genre_bp.route("/books/<int:book_id>/genres/", methods=["POST"])
@jwt_required()
def add_genre(book_id):
    # Get the data from the body of the request
    body_data = request.get_json()
    
    # Load and validate genre data
    genre_name = body_data.get("genre_name")
    if genre_name not in ALLOWED_GENRES:
        return {"error": f"Genre '{genre_name}' is not allowed. Allowed genres are: {', '.join(ALLOWED_GENRES)}."}, 400  # Bad Request

    genre = genre_schema.load(body_data)

    # Fetch the book with the id=book_id
    stmt = db.select(Book).filter_by(id=book_id)
    book = db.session.scalar(stmt)

    # Check if the book exists
    if book:
        # Count the number of existing genres for the specified genre_name
        existing_genre_count = db.session.query(Genre).filter_by(genre_name=genre_name).count()

        # Check if the existing count exceeds the limit
        if existing_genre_count >= 10:
            return {"error": f"There cannot be more than 10 genres of '{genre_name}' at a time."}, 400  # Bad Request

    
        # Create instance of genre model
        genre = Genre(genre_name=genre_name)

        # Associate genre with the book if needed, or manage relationships accordingly
        db.session.add(genre)
        db.session.commit()
        
        # Return acknowledgement
        return {"message": f"Genre '{genre.genre_name}' successfully added to the book '{book.title}'!"}, 201  # Created
    else:
        # Return error if the book doesn't exist
        return {"error": f"A book with id {book_id} does not exist!"}, 404  # Not Found
    
# DELETE - remove an author from a specific book | /books/<book_id>/authors/
@genre_bp.route("/books/<int:book_id>/genres", methods=["DELETE"])
@jwt_required()
def delete_genre(book_id):
    # Fetch the book with the id=book_id
    book_stmt = db.select(Book).filter_by(id=book_id)
    book = db.session.scalar(book_stmt)

    # Check if the book exists
    if book:
        # Check if the book has an associated author
        if book.genre_id is not None:
            # Unassign the author
            book.genre_id = None  # Remove the association with the author
            
            db.session.commit()
            
            return {"message": f"Genre has been removed from the book '{book.title}'!"}, 200  # Request Successful
        else:
            return {"error": f"The book '{book.title}' has no associated genre."}, 400  # Bad Request
    else:
        # Return error if the book doesn't exist
        return {"error": f"A book with id {book_id} does not exist!"}, 404  # Not Found


# PUT/PATCH - update a specific genre associated with a book | /books/<book_id>/genres/<genre_id>
@genre_bp.route("/books/<int:book_id>/genres/", methods=["PUT", "PATCH"])
@jwt_required()
def edit_genre(book_id):
    # Get the data from the body of the request
    body_data = request.get_json()
    genre_name = body_data.get("genre_name")
    
    # Validate genre name
    if genre_name not in ALLOWED_GENRES:
        return {"error": f"Genre '{genre_name}' is not allowed. Allowed genres are: {', '.join(ALLOWED_GENRES)}."}, 400  # Bad Request

    # Fetch the book with the id=book_id
    book_stmt = db.select(Book).filter_by(id=book_id)
    book = db.session.scalar(book_stmt)

    # Check if the book exists
    if book:
        # Fetch or create the genre
        genre_stmt = db.select(Genre).filter_by(genre_name=genre_name)
        genre = db.session.scalar(genre_stmt)

        if not genre:
            # Create a new genre if it doesn't exist
            genre = Genre(genre_name=genre_name)
            db.session.add(genre)

        # Update the book's genre
        book.genre_id = genre.id  # Associate the book with the genre

        db.session.commit()
        
        # Return acknowledgment
        return {"message": f"Genre for book '{book.title}' successfully updated to '{genre.genre_name}'!"}, 200  # Updated
    else:
        # Return error if the book doesn't exist
        return {"error": f"A book with id {book_id} does not exist!"}, 404  # Not Found
