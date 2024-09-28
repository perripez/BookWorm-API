from init import db, ma
from marshmallow import fields

class Genre(db.Model):
    # Name of the table
    __tablename__ = "genre"
    # Attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String, nullable=False)

    # Define the relationship to book
    books = db.relationship("Book", back_populates="genre")

class GenreSchema(ma.Schema):
    books = fields.List(fields.Nested("BookSchema", exclude=["genre"]))

    class Meta:
        fields = ("id", "genre_name")

# To handle a single genre object
genre_schema = GenreSchema()
# To handle multiple genre objects
genres_schema = GenreSchema(many=True)
