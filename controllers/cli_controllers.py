from datetime import date
from flask import Blueprint
from sqlalchemy import text

from init import db, bcrypt
from models.user import User
from models.book import Book
from models.review import Review

db_commands = Blueprint("db", __name__)

# Create Tables Command
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables Created!")

# Seed Tables Command
@db_commands.cli.command("seed")
def seed_tables():
    # Create a list of user instances - Dummy Values
    users = [
        User(
            name = "Book Worm",
            email = "admin@bookworm.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin = True
        ),
        User(
            name = "Perri Adkins",
            email = "perri@gmail.com",
            password = bcrypt.generate_password_hash("abcdef").decode("utf-8"),
        )
    ]

    db.session.add_all(users)

    books = [
        Book(
            title = "Book 1",
            publication_year = "2000",
            date = date.today(),
            user = users[0]
        ),
        Book(
            title = "Book 2",
            publication_year = "2004",
            date = date.today(),
            user = users[0]
        ),
        Book(
            title = "Book 3",
            publication_year = "2021",
            date = date.today(),
            user = users[1]
        )
    ]

    db.session.add_all(books)

    db.session.commit()
    print("Tables Seeded!")

# Drop Tables Command
@db_commands.cli.command("drop")
def drop_tables():
    # Close any active sessions
    db.session.close()
    
    # Manually drop tables with CASCADE to handle dependencies
    db.session.execute(text('DROP TABLE IF EXISTS books CASCADE;'))
    db.session.execute(text('DROP TABLE IF EXISTS users CASCADE;'))
    db.session.commit()

    # Optionally drop all remaining tables
    db.drop_all()
    print("Tables Dropped!")