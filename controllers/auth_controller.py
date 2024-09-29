from flask import Blueprint, request
from models.user import User, user_schema
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token
from datetime import timedelta
from models.user import  UserSchema
from init import bcrypt, db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# User registration route
@auth_bp.route("/register", methods=["POST"])
def register_user():
    user_schema = UserSchema()
    try:
        # Get the data from the body of the request
        body_data = request.get_json()
        user = user_schema.load(body_data)
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
        return user_schema.dump(user), 201 # Created 
    # If user data not entered correctly, return error
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return{"error": f"Your {err.orig.diag.column_name} is required"}, 400 # Bad Request 
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return{"error": "Email already in use"}, 400 # Bad Request 

# User login route
@auth_bp.route("/login", methods=["POST"])
def login_user():
    # Get the data from the body of the request
    body_data = request.get_json()
    # Find the user in the db with that specific email address
    stmt = db.select(User).filter_by(email=body_data.get("email")) # SELECT * FROM users WHERE email = 'email_value';
    user = db.session.scalar(stmt)
    # If user exists + password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")): # Check from db, map with data from request
        # Create JWT
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=3)) # Session expires in 3 days
        # Return acknowledgement
        return {"email": user.email, "is_admin": user.is_admin, "token": token}
    # Else
    else:
        # Return error
        return {"Error": "Invalid email or password"}, 400 # Bad Request