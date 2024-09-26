from init import db, ma
from marshmallow import fields # Serialise and Deserialise data with Marshmallow

class Book(db.Model):
    # Name of the table
    ___tablename__ = "books"
    # Attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    publication_year = db.Column(db.Year) # YYYY

    # Define foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Define relationship
    user = db.relationship('User', back_populates='cards')

class BookSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=["id", "name", "email"]) # Unpack user value with schema - only id, name + email

    class Meta:
        fields = ("id", "title", "publication_year", "user")

# To handle single user object
book_schema = BookSchema()
# To handle multiple user objects
books_schema = BookSchema(many=True)

    
