from datetime import date
from flask import Blueprint
from sqlalchemy import text

from init import db, bcrypt
from models.user import User
from models.book import Book
from models.review import Review
from models.author import Author

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
    db.session.commit()

    # Create a list of author instances - Dummy Values
    authors = [
        Author(
            first_name = "Author",
            last_name = "One",
        ),
        Author(
            first_name = "Author",
            last_name = "Two",
        ),
        Author(
            first_name = "Author",
            last_name = "Three",
        )
    ]

    db.session.add_all(authors)
    db.session.commit()

    # Create a list of book instances - Dummy Values
    books = [
        Book(
            title = "Book 1",
            publication_year = "2000",
            date = date.today(),
            user_id = users[0].id,
            author_id = authors[0].id
        ),
        Book(
            title = "Book 2",
            publication_year = "2004",
            date = date.today(),
            user_id = users[0].id,
            author_id = authors[1].id
        ),
        Book(
            title = "Book 3",
            publication_year = "2021",
            date = date.today(),
            user_id = users[1].id,
            author_id = authors[2].id
        )
    ]

    db.session.add_all(books)
    db.session.commit()

    # Create a list of review instances - Dummy Values
    reviews = [
        Review(
            rating = "5",
            comment = "Very Good",
            date = date.today(),
            user_id = users[0].id,
            book_id = books[0].id
        ),
          Review(
            rating = "4",
            comment = "Good",
            date = date.today(),
            user_id = users[1].id,
            book_id = books[1].id
        ),
          Review(
            rating = "3",
            comment = "Okay",
            date = date.today(),
            user_id = users[0].id,
            book_id = books[2].id
        )
    ]

    db.session.add_all(reviews)
    db.session.commit()

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