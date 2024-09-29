from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required 

from init import db
from models.review import Review, review_schema, reviews_schema
from models.book import Book, book_schema, books_schema
from utils import auth_as_admin_decorator

reviews_bp = Blueprint("reviews", __name__, url_prefix="/<int:book_id>/reviews")

# GET - fetch all reviews | /book_id/reviews - NOT NEEDED

# POST - create a new review | /book_id/reviews
@reviews_bp.route("/", methods=["POST"])

@jwt_required()
def create_review(book_id):
    # Get the data from the body of the request
    body_data = request.get_json()
    review = review_schema.load(body_data)
    # Fetch the book with id=book_id
    stmt = db.select(Book).filter_by(id=book_id)
    # SELECT * FROM books WHERE id = 'book_id value';
    book = db.session.scalar(stmt)
    # if book exists
    if book:
        # Create instance of review model
        review = Review(
            rating = body_data.get("rating"),
            comment = body_data.get("comment"),
            date = date.today(),
            user_id = get_jwt_identity(),
            book_id = book.id
        )
        # Commit session to db
        db.session.add(review)
        db.session.commit()
        # return acknowledgement
        return review_schema.dump(review), 201 # Created
    # Else
    else:
        # Return error
        return {"error": f"A book with id {book_id} does not exist!"}, 404 # Bad Request
    

# DELETE - delete a specific review from a book | /books/<book_id>/reviews/<review_id>
@reviews_bp.route("/<int:review_id>/", methods=["DELETE"])
@jwt_required()
# Ensure only admins can delete a review
@auth_as_admin_decorator
def delete_review(book_id, review_id):
    # Fetch the review from the db
    stmt = db.select(Review).filter_by(id=review_id)
    # SELECT * FROM reviews WHERE id = 'review_id value';
    review = db.session.scalar(stmt)
    # If the review exits
    if review:
        # Delete the review
        db.session.delete(review)
        db.session.commit()
        # Return acknowledgement
        return {"message": f"Review with message {review.comment} deleted successfully!"}, 200 # Request successful
    # Else
    else:
        # Return error
        return {"error": f"Review with id {review_id} does not exist!"}, 404 # Bad Request
    

# PUT,PATCH - update a specific review from a book | /books/<book_id>/reviews/<review_id>
@reviews_bp.route("/<int:review_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_review(book_id, review_id):
    # Get the data from the body of the request
    body_data = request.get_json()
    review = review_schema.load(body_data)
    # Fetch the review from the db
    stmt = db.select(Review).filter_by(id=review_id)
    # ^ SELECT * FROM reviews WHERE id = 'review_id value';
    review = db.session.scalar(stmt)
    # If the review exits
    if review:
        # Update the review fields as required
        review.rating = body_data.get("rating") or review.rating
        review.comment = body_data.get("comment") or review.comment
        # Commit to the db
        db.session.commit()
        # Return acknowledgement
        return review_schema.dump(review), 200 # Updated successfully
    # Else
    else:
        # Return an error message
        return {"error": f"Review with id {review_id} not found!"}, 400 # Bad Request

