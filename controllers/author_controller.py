from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from init import db
from models.author import Author, author_schema, authors_schema
from models.book import Book, book_schema, books_schema

author_bp = Blueprint("authors", __name__, url_prefix="/authors")

# GET - fetch all authors | /authors
@author_bp.route("/", methods=["GET"])
def get_all_authors():
    stmt = db.select(Author) # SELECT * FROM authors
    authors =db.session.scalars(stmt)
    return authors_schema.dump(authors)