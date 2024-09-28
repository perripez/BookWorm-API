from init import db, ma
from marshmallow import fields # Serialise and Deserialise data with Marshmallow


class Book(db.Model):
    # Name of the table
    __tablename__ = "books"
    # Attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    publication_year = db.Column(db.Integer) # YYYY
    date = db.Column(db.Date)

    # Define foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))

    # Define relationships
    user = db.relationship("User", back_populates="books")
    reviews = db.relationship("Review", back_populates="book", cascade="all, delete")
    author = db.relationship("Author", back_populates="books")

class BookSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["id", "name", "email"]) # Unpack user value with schema - only id, name + email
    reviews = fields.List(fields.Nested("ReviewSchema", only=["rating"]))
    author = fields.Nested("AuthorSchema", only=["first_name", "last_name"])

    class Meta:
        fields = ("id", "title", "publication_year", "author", "date", "user", "reviews")
        include_fk = True
        ordered = True

# To handle single user object
book_schema = BookSchema()
# To handle multiple user objects
books_schema = BookSchema(many=True)

    
