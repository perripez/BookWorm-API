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
        return {"error": f"Author with id {genre_id} not found!"}

# POST - create a new genre entry | /book_id/genres
@genre_bp.route("/books/<int:book_id>/genres/", methods=["POST"])
@jwt_required()
def add_genre(book_id):
    # Get the data from the body of the request
    body_data = request.get_json()
    # Fetch the book with the id=book_id
    stmt = db.select(Book).filter_by(id=book_id)
    # SELECT * FROM books WHERE id = 'book_id value';
    book = db.session.scalar(stmt)
    # if the book exists
    if book:
        # Create instance of genre model
        genre = Genre(
            genre_name = body_data.get("genre_name")
        )

        # Commit to the db
        db.session.add(genre)
        db.session.commit()

        book.genre_id = genre.id
        db.session.commit()

        # Return acknowledgement
        return {"message": f"Genre {genre.genre_name} successfully added to the book {book.title}!"}, 200 # Created successfully
    # Else
    else:
        #  Return error
        return {"error": f"A book with id {book_id} does not exist!"}, 404 # Bad Request
    
# DELETE - delete a specific genre from a book | /books/<book_id>/genres/<genre_id>
@genre_bp.route("/genres/<int:genre_id>", methods=["DELETE"])
@jwt_required()
def delete_genre(genre_id):
    # Fetch the genre from the db
    stmt = db.select(Genre).filter_by(id=genre_id)
    # SELECT * FROM  genres WHERE id = 'author_id value';
    genre = db.session.scalar(stmt)
    # If the genre exists
    if genre:
        # Delete the author
        db.session.delete(genre)
        db.session.commit()
        # Return acknowledgement
        return {"message": f"Genre {genre.genre_name} has been deleted successfully!"}, 200 # Request Successful
    # Else:
    else:
        # Return error
        return {"error": f"Genre with the id {genre_id} does not exist!"}, 404 # Bad Request
    
# PUT/PATCH - update a specific author | /authors/<author_id>

@genre_bp.route("/genres/<int:genre_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_genre(genre_id):
    # Get the data from the body of the request
    body_data = request.get_json()
    # Fetch the author from the database
    stmt = db.select(Genre).filter_by(id=genre_id)
    # SELECT * FROM authors WHERE id = 'genre_id value';
    genre = db.session.scalar(stmt)
    # If the genre exists
    if genre:
        # Update the reveiw fields as required
        genre.genre_name = body_data.get("genre_name") or genre.genre_name
        # Commit to the db
        db.session.commit()
        # Return acknowledgement
        return genre_schema.dump(genre), 200 # Updated Successfully
    # Else
    else:
        # Return an error message
        return {"error": f"Genre with id {genre_id} not found!"}, 400 # Bad Request
