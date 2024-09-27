from init import db, ma
from marshmallow import fields

class Review(db.Model):
    # Name of the table
    __tablename__ = "reviews"
    # Attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)

    # Define foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)

    # Define relationships
    user = db.relationship("User", back_populates="reviews")

    book = db.relationship("Book", back_populates="reviews")

class ReviewSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["name", "email"]) # Unpack user value with schema - only id, name + email

    book = fields.Nested("BookSchema", exclude=["user"])

    class Meta:
        fields = ("id", "rating", "comment", "date", "user", "book")

# To handle single user object
review_schema = ReviewSchema()
# To handle multiple user objects
reviews_schema = ReviewSchema(many=True)