from init import db, ma
from marshmallow import fields, validate

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

class BookSimpleSchema(ma.Schema):
    id = fields.Integer()
    title = fields.String()

class ReviewSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["name", "email"]) # Unpack user value with schema - only id, name + email

    # Validate that ratings are 1,2,3,4 or 5 stars
    rating = fields.Integer(
        required=True, validate=validate.OneOf([1, 2, 3, 4, 5], error="Rating must be between 1 and 5 stars."))
    
    class Meta:
        fields = ("id", "rating", "comment", "date", "user")

# To handle single review object
review_schema = ReviewSchema()
# To handle multiple review objects
reviews_schema = ReviewSchema(many=True)