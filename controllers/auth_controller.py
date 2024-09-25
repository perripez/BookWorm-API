from flask import Blueprint, request
from models.user import User, user_schema
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

from init import bcrypt, db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# User registration route
@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # Get the data from the body of the request
        body_data = request.get_json()
        # Create an instance of the user model
        user = User(
            name = body_data.get("name"),
            email = body_data.get("email")
        )
        # Hash the password
        password = body_data.get("password")
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        # Add + Commit to the database
        db.session.add(user)
        db.session.commit()
        # Return acknowledgement
        return user_schema.dump(user), 201 # Created code
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return{"error": f"Your {err.orig.diag.column_name} is required"}, 400
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return{"error": "Email already in use"}, 400

# User login route
# @auth_bp.route("/login")