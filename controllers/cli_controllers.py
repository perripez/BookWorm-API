from flask import Blueprint

from init import db, bcrpyt
from models.user import User

db_commands = Blueprint("db", __name__)

# Create Tables Command
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables Created!")

# Seed Tables Command
@db_commands.cli.command("seed")
def seed_tables():
    # Create a list of user instances
    users = [
        User(
            name = "Book Worm",
            email = "admin@bookworm.com",
            password = bcrpyt.generate_password_hash("123456").decode("utf-8"),
            is_admin = True
        ),
        User(
            name = "Perri Adkins",
            email = "perri@gmail.com",
            password = bcrpyt.generate_password_hash("abcdef").decode("utf-8"),
        )
    ]

    db.session.add_all(users)

    db.session.commit()
    print("Tables Seeded!")

# Drop Tables Command
@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables Dropped!")