from init import db, ma
from marshmallow import fields, validates, ValidationError
import re

class User(db.Model):
    # Name of the table
    __tablename__ = "users"

    # Attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    books = db.relationship('Book', backref='user', lazy=True)  # Ensure this line is present


    # Define relationship
    books = db.relationship("Book", back_populates="user")

    reviews = db.relationship("Review", back_populates="user")

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

class UserSchema(ma.Schema):

    books = fields.List(fields.Nested('BookSchema', exclude=["user"]))

    reviews = fields.List(fields.Nested('ReviewSchema', exclude=["user"]))

    @validates("email")
    def validate_email(self, value):
        if not re.match(EMAIL_REGEX, value):
            raise ValidationError("Invalid email format")

    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "books", "reviews")

# To handle single user object
user_schema = UserSchema(exclude=["password"])
# To handle multiple user objects
users_schema = UserSchema(many=True, exclude=["password"])
