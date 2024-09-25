from init import db, ma

class User(db.Model):
    # Name of the table
    __tablename__ = "users"

    # Attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "password", "is_admin")

# To handle single user object
user_schema = UserSchema(exclude=["password"])
# To handle multiple user objects
users_schema = UserSchema(many=True, exclude=["password"])
