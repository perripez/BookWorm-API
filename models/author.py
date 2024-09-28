from init import db, ma
from marshmallow import fields

class Author(db.Model):
    # Name of the table
    __tablename__ = "authors"
    # Attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    
    # Define relationship to book
    books = db.relationship("Book", back_populates="author")

class AuthorSchema(ma.Schema):
    books = fields.List(fields.Nested("BookSchema", exclude=["author", "reviews"]))
    
    class Meta:
        fields = ("id", "first_name", "last_name", "books")

# To handle single author object
author_schema = AuthorSchema()
# To handle multiple author objects
authors_schema = AuthorSchema(many=True)
