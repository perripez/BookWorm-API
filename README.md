# BookWorm_API
## T2A3_PerriAdkins

### Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

The BookWorm API solves the problem of tracking a keeping a consise book collection of reviewed books. A user will be able to login, add books to their collection (linked to Authors and Genres) and leave reviews for each book. 

- **User Management:**
The BookWorm API allows users to register, log in, and manage their accounts securely using JWT (JSON Web Tokens) for authentication. This ensures that user data is protected and accessible only to authorised users.

    Administrators have the capability to manage user accounts effectively, including the ability to delete users when necessary, ensuring a clean and controlled user base.

- **Book Organisation**
Users can create and manage a library of books, allowing them to add books they own or wish to read.

    The API also supports retrieving information about books, helping users access the data they need without the hassle of managing physical records.

- **Review System:**
The API includes features that allow users to write and manage reviews for books. This encourages engagement and provides valuable insights to other readers. Users can read reviews from their peers, aiding them in making informed choices about their reading selections.

    By linking reviews to specific users and books, the app fosters a community feel, encouraging interaction among users.

- **Data Integrity and Relationships:**
Using an ORM (Object-Relational Mapping) like SQLAlchemy, the API maintains data integrity by enforcing relationships between users, books, and reviews. This means users cannot lose track of which reviews belong to which books or users, as the system will manage these relationships automatically.

    Cascading deletions ensure that when a user is deleted, their associated reviews and books are handled appropriately, preventing orphaned records.

- **Scalability and Maintenance:**
The architecture of the API supports future enhancements and additional features without significant rework.
___

### Describe the way tasks are allocated and tracked in your project.

To track this project, I am using GitHub Projects. Similar to Trello, GitHub projects uses a Kanban model to allow smaller subtasks to be allocated to a 'To-Do', 'In Progress' and 'Done' column.

#### Screenshots of task progress:

**24/9/24**
![GitHub_tasks_1](./docs/Task%20Progress/Tasks1.png)

**25/9/24**
![GitHub_tasks_2](./docs/Task%20Progress/Tasks2.png)

**26/9/24**
![GitHub_tasks_3](./docs/Task%20Progress/Tasks3.png)

**27/9/24**
![GitHub_tasks_4](./docs/Task%20Progress/Tasks4.png)

**28/9/24**
![GitHub_tasks_5](./docs/Task%20Progress/Tasks5.png)

**29/9/24**
![GitHub_tasks_6](./docs/Task%20Progress/Tasks6.png)

___

### List and explain the third-party services, packages and dependencies used in this app.

- **Flask**
Flask is a lightweight web framework for Python. It allows developers to create web applications quickly and easily by providing tools for routing, handling requests, and managing templates. Flask follows a minimalistic approach, meaning it provides only the essentials and allows you to add extensions as needed. It's often used for small to medium web projects and is popular due to its flexibility, simplicity, and ease of use.

- **PostgreSQL**
PostgreSQL is an advanced, open-source relational database system. It supports SQL for querying and managing data and includes features like data integrity, complex queries, and transactional processing. PostgreSQL is known for its reliability, extensibility, and ability to handle large-scale applications. It supports JSON, making it versatile for modern applications, and is widely used in both small projects and large enterprise systems.

- **Marshmallow**
Marshmallow is a Python library used for object serialisation and deserialisation. It helps convert complex data types, like objects, into Python data structures (like dictionaries) that can be easily stored or transmitted, and vice versa. It's commonly used for validating input data and transforming it into a format that can be saved in a database or returned in API responses. Marshmallow is lightweight and integrates well with web frameworks like Flask.

- **SQLAlchemy**
SQLAlchemy is a Python library for working with databases using an Object Relational Mapping (ORM) system. It allows developers to interact with databases using Python objects instead of writing raw SQL queries. SQLAlchemy provides a flexible and powerful toolkit for database management, offering high-level ORM capabilities as well as a lower-level SQL expression language for more direct database interactions. It's widely used for its efficiency and versatility in handling different types of databases.

- **Psycopg2**
Psycopg2 is a popular PostgreSQL adapter for the Python programming language. It allows Python applications to connect to and interact with PostgreSQL databases, enabling operations like querying, data manipulation, and transaction management. Psycopg2 is designed to be efficient and compliant with the Python database API 2.0 specification. It supports advanced PostgreSQL features, making it a preferred choice for developers working with PostgreSQL in Python applications.

- **Bcrypt**
Bcrypt is a password hashing function designed for secure password storage. It applies a strong cryptographic algorithm to hash passwords, making it difficult for attackers to reverse-engineer the original password. Bcrypt includes a built-in mechanism for incorporating a salt to protect against rainbow table attacks and allows the adjustment of the hashing workload to enhance security as computing power increases. It’s widely used in applications that require secure user authentication and is known for its robustness and resistance to brute-force attacks.

- **JWT Manager**
JWT Manager is a library used for handling JSON Web Tokens (JWT) in applications. It simplifies the process of creating, signing, verifying, and decoding JWTs, which are widely used for secure authentication and information exchange between parties. JWT Manager typically supports features such as token expiration, signature verification, and claims handling. It is commonly used in web and mobile applications to manage user sessions and ensure secure communication between clients and servers.

___

### Explain the benefits and drawbacks of this app’s underlying database system.

For the BookWorm API, I have decided to use PostgreSQL.

**Benefits:**

- Open source and free
- *Extensibility:*
Users can create custom data types, operators, and functions. PostgreSQL is highly customisable for various applications.
- *ACID Compliance:*
PostgreSQL fully supports ACID (Atomicity, Consistency, Isolation, Durability) properties, ensuring data reliability and integrity.
- *Support for Complex Queries:*
PostgreSQL has excellent support for complex queries, joins, views, and subqueries. It's highly efficient when working with large datasets and supports SQL standards like JSON, XML, and arrays.
- *Cross-Platform Compatibility:*
It can run on most major operating systems, including Linux, macOS, and Windows, making it versatile across development environments.
- *Active Community and Documentation:*
PostgreSQL has a strong community and extensive documentation, which helps developers troubleshoot and implement solutions quickly.

**Drawbacks:**

- *Performance in Write-Heavy Workloads:*
While PostgreSQL handles complex queries efficiently, it may lag behind other databases (like MySQL) in handling heavy write operations, especially in extremely large datasets.
- *Resource Intensive:*
PostgreSQL tends to consume more memory and CPU resources compared to lighter databases like MySQL, making it less suitable for applications with constrained hardware.
- *Learning Curve:*
Due to its advanced features and flexibility, PostgreSQL may have a steeper learning curve for beginners or those coming from simpler databases like MySQL or SQLite.

https://www.postgresql.org/docs/

___

### Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

For the BookWorm API, I have decided to use SQLAlchemy in Python.

**ORM Explained:**
SQLAlchemy ORM (Object Relational Mapper) is a powerful tool in Python that allows developers to interact with databases using Python objects instead of writing raw SQL queries. It abstracts the complexities of database operations and maps database tables to Python classes, making it easier to perform CRUD (Create, Read, Update, Delete) operations.

**Features:**

- *Schema Definition and Generation:*
SQLAlchemy allows developers to define their database schemas in Python, and these schemas can be used to create tables automatically in the database. This declarative approach makes database schema management easier.
- *Session Management:*
QLAlchemy's ORM uses a session to manage the lifecycle of Python objects in relation to the database. The session handles queries, updates, transactions, and more, maintaining state consistency between your Python objects and database rows.
- *Data Validation and Constraints:*
SQLAlchemy allows defining constraints (e.g., primary keys, foreign keys, unique constraints) and data validation rules directly in your Python models. This ensures that your database schema is properly enforced at the application level.
- *Relationship Management:*
SQLAlchemy ORM can handle one-to-many, many-to-one, one-to-one, and many-to-many relationships between tables, making it easy to work with complex data structures.

**Purpose:**
- Simplify database access for developers.
- Provide flexibility in database interactions (ORM for convenience, SQL for complex operations).
- Work with multiple database systems (SQLite, MySQL, PostgreSQL, Oracle, etc.) while writing minimal database-specific code.

**Functionalities:**
- *Data Modeling:*
SQLAlchemy allows defining and manipulating tables, relationships, and constraints using Python objects. This ensures that the data structure is easily manageable and modifiable.

Example:
```
class Genre(db.Model):
    # Name of the table
    __tablename__ = "genres"
    # Attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String, nullable=False)

    # Define the relationship to book
    books = db.relationship("Book", back_populates="genre")

    ALLOWED_GENRES = {"Self help", "Autobiography", "Fiction", "Health", "Children's"}
```

- *CRUD Operations:*
The ORM layer allows simple creation, reading, updating, and deletion of records using Python objects without needing to write SQL queries.

Examples:
```
# GET - fetch all books in db | /books
@books_bp.route("/")
def get_all_books():
    stmt = db.select(Book) # SELECT * FROM books
    books = db.session.scalars(stmt)
    return jsonify(books_schema.dump(books))

# DELETE - delete a specific book from db | /books/<id>
@books_bp.route("/<int:book_id>", methods=["DELETE"])
@jwt_required()
def delete_book(book_id):
    # Fetch the book from the db
    stmt = db.select(Book).filter_by(id=book_id)
    # ^ SELECT * FROM books WHERE id = 'book_id value';
    book = db.session.scalar(stmt)
    # If the book exists
    if book:
        # Delete the book
        db.session.delete(book)
        db.session.commit()
        return {"message": f"Book with id {book_id} has been deleted"}, 200 # Request successful
    # Else
    else:
        # Return error
        return{"error": f"Book with id {book_id} does not exist!"}, 404 # Bad Request
```


- *Querying:*
SQLAlchemy allows complex data queries using Python’s syntax. You can query for specific data, filter results, and join tables as if you're working with Python lists and objects.

Example:
```
    # Fetch the review from the db
    stmt = db.select(Review).filter_by(id=review_id)
    # ^ SELECT * FROM reviews WHERE id = 'review_id value';
```

https://docs.sqlalchemy.org/en/20/orm/session_basics.html 

___

### Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. 

The BookWorm API contains the following tables:

- User: Identified by user_id (Primary Key), allows users to set a name, email and password to log in. Reviews can only be deleted by admins and entries can only be edited by the user who creates them

- Book: 1 user can have many books. The book table is related to the user, author and genre with a foreign key. Users can enter the book title and publication year.

- Review: 1 book can have many reviews. The review table is related to the user and book with a foreign key. Users can enter a rating (1 star, 2 stars, 3 stars, 4 stars, 5 stars), comment and the date created will be automatically assigned.

- Author: Books can have 1 author. Users can enter the first name and last name of the author.

- Genre: Books can have 1 genre. Users can enter a genre (Self Help, Fiction, Health, Childrens, Autobiography).

![BookWorm_ERD](./docs/BookWorm%20ERD.png)
___
___

*AFTER DEVELOPMENT HAS BEGUN*

### Explain the implemented models and their relationships, including how the relationships aid the database implementation.

Since completing the API, the updated models are below:

- **Users**
Attributes:
`id:` The primary key for identifying each user.
`name:` The name of the user.
`email:` The email of the user, which must be unique.
`password:` The hashed password for user authentication.
`is_admin:` A boolean flag indicating if the user has admin privileges.

Relationships:
Books: A one-to-many relationship with the `Book` model, where a user can have multiple books. This is defined using `db.relationship("Book", back_populates="user", cascade="all, delete-orphan")`. The `cascade` option means that if a user is deleted, all their associated books will also be deleted.

Reviews: A one-to-many relationship with the `Review` model, indicating that a user can leave multiple reviews.

- **Books**
Attributes:
`id:` The primary key for identifying each book.
`title:` The title of the book.
`year_published:` The year the book was published.
*UPDATED IN DEVELOPMENT* `date:` The day the book was added.

`user_id:` A foreign key that references the User model, indicating which user owns the book.
`author_id:` A foreign key that reference the Author model, indicating the author assigned to the book
`genre_id:`A foreign key that reference the Genre model, indicating the genre assigned to the book

Relationships
User: A many-to-one relationship with the `User` model, where each book is associated with a single user (owner).

Reviews: A one-to-many relationship with the `Review` model, indicating that a book can have multiple reviews.

Author: A many-to-one relationship with the `Author` model, indicating that many books can have an author.

Genre: A many-to-one relationship with the `Genre` model, indicating that many books can have a genre.

- **Reviews**

`id:` The primary key for identifying each review.
`rating:` The rating of the book
`comment:` The review of the book
`date:` Date the review was added

`user_id:` A foreign key that references the User model, indicating which user owns the review.
`book_id:` A foreign key that references the Book model, indicating which book the review is for.

Relationships:
Book: A many-to-one relationship with the `Book` model, where each review is associated with a single book.

User: A many-to-one relationship with the `User` model, where each review is written by a single user.

- **Authors**
`id:` The primary key for identifying each author
`first_name:` The first name of the author
`last_name:` The last name of the author

Relationships:
Book: A one-to-many relationship with the `Book` model, where each author is associated with many books.

- **Genres**
`id:` The primary key for identifying each author
`genre_name:` The genre

Relationships:
Book: A one-to-many relationship with the `Book` model, where each genre is associated with many books.

**Extra Features**

- Review ratings can only be `[1,2,3,4,5] Stars`
- Genres can only be `["Self help", "Autobiography", "Fiction", "Health", "Children's"]`
- There can only be up to 10 of each Genre in the database at once
- Only admin can delete a user or review
- Publication year must be in te `YYYY` format, between 1450-`current_year`
- Emails are validated when users register

Overall, during the development, the only change I made to my ERD was including a `date` column for the entries. This makes it easier to keep track of when books were entered, and how long they have been in the database for.

**Updated ERD:**
![Updated_ERD](./docs/Updated%20ERD.png)


___

### Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:

#### USERS

**Login**
- POST
- http://localhost:8080/auth/login
- JSON body data: "email", "password"
- Response: User is either looged in with correct login information (200)
![User_login](./docs/End%20Points/USER/User.login.png)
or recieves an error (400)
![User_login_error](./docs/End%20Points/USER/User.login.error.png)

**Register**
- POST
- http://localhost:8080/auth/register
- JSON body data: "name", "email", "password"
- Response: A new user is created (201)
![User_register](./docs/End%20Points/USER/User.register.png)
or user recieves an error (500)
![User_register_error](./docs/End%20Points/USER/User.register.error.png)

**Delete User - ADMIN ONLY**
- DELETE
- http://localhost:8080/auth/users/<int:user_id>
- Admin Token required
- Response: The user is deleted (200)
![User_delete](./docs/End%20Points/USER/User.delete.png)
or user recieves an error (403)
![User_delete_error](./docs/End%20Points/USER/User.delete.error.png)

#### BOOKS

**View all books**
- GET
- http://localhost:8080/books
- User must be logged in
- Response: All books in database displayed (200)
![Books_getall](./docs/End%20Points/BOOK/Books.getall.png)

**View specific book**
- GET
- http://localhost:8080/books/<int:book_id>
- User must be logged in
- Response: Specific book is displayed (200)
![Books_getbook](./docs/End%20Points/BOOK/Books.getbook.png)
or user recieves an error (404)
![Books_getbook_error](./docs/End%20Points/BOOK/Books.getbook.error.png)

**Create a book**
- POST
- http://localhost:8080/books/
- User must be logged in, JSON body data: "title", "publication_year"
- Response: Book is created (201)
![Books_create](./docs/End%20Points/BOOK/Books.create.png)
or user recieves an error (404)
![Books_create_error](./docs/End%20Points/BOOK/Books.create.error.png)

**Delete a book**
- DELETE
- http://localhost:8080/books/<int:book_id>
- User must be logged in
- Response: Book is deleted (200)
![Books_delete](./docs/End%20Points/BOOK/Books.delete.png)
or user recieves an error (404)
![Books_delete_error](./docs/End%20Points/BOOK/Books.delete.error.png)

**Update a book**
- PUT/PATCH
- http://localhost:8080/books/<int:book_id>
- User must be logged in, JSON body data: "title", "publication_year"
- Response: Book is updated (201)
![Books_update](./docs/End%20Points/BOOK/Books.update.png)
or user recieves an error (404) or (400)
![Books_update_error1](./docs/End%20Points/BOOK/Books.update.error1.png)
![Books_update_error2](./docs/End%20Points/BOOK/Books.update.error2.png)

#### REVIEWS

**Create a review**
- POST
- http://localhost:8080/books/<int:book_id>/reviews
- User must be logged in, JSON body data: "rating", "comment"
- Response: Review is created (201)
![Reviews_create](./docs/End%20Points/REVIEWS/Reviews.create.png)
or user recieves an error (500) or (404)
![Reviews_create_error1](./docs/End%20Points/REVIEWS/Reviews.create.error1.png)
![Reviews_create_error2](./docs/End%20Points/REVIEWS/Reviews.create.error2.png)

**Delete a review**
- DELETE
- http://localhost:8080/books/<int:book_id>/reviews/<int:review_id>
- User must be an admin
- Response: Review is deleted (200)
![Reviews_delete](./docs/End%20Points/REVIEWS/Reviews.delete.png)
or user recieves an error (403) or (404)
![Reviews_delete_error1](./docs/End%20Points/REVIEWS/Reviews.delete.error1.png)
![Reviews_delete_error2](./docs/End%20Points/REVIEWS/Reviews.delete.error2.png)

**Edit a review**
- PUT/PATCH
- http://localhost:8080/books/<int:book_id>/reviews/<int:review_id>
- User must logged in, JSON body data: "rating", "comment"
- Response: Review is edited (200)
![Review_update](./docs/End%20Points/REVIEWS/Review.update.png)
or user recieves an error (500) or (400)
![Review_update_error1](./docs/End%20Points/REVIEWS/Review.update.error1.png)
![Review_update_error2](./docs/End%20Points/REVIEWS/Review.update.error2.png)

#### AUTHORS

**View all authors**
- GET
- http://localhost:8080/authors
- User must be logged in
- Response: All authors in database displayed (200)
![Authors_getall](./docs/End%20Points/AUTHORS/Authors.getall.png)

**View specific author**
- GET
- http://localhost:8080/authors/<int:author_id>
- User must be logged in
- Response: Specific author is displayed (200)
![Authors_getauthor](./docs/End%20Points/AUTHORS/Authors.getauthor.png)
or user recieves an error (404)
![Authors_getauthor_error](./docs/End%20Points/AUTHORS/Authors.getauthor.error.png)

**Create an author**
- POST
- http://localhost:8080/books/<int:book_id>/authors
- User must be logged in, JSON body data: "first_name", "last_name"
- Response: Author is created (200)
![Authors_create](./docs/End%20Points/AUTHORS/Authors.create.png)
or user recieves an error (404)
![Authors_create_error](./docs/End%20Points/AUTHORS/Authors.create.error.png)

**Delete an author**
- DELETE
- http://localhost:8080/books/<int:book_id>/authors
- User must be logged in
- Response: Author is deleted (200)
![Authors_delete](./docs/End%20Points/AUTHORS/Authors.delete.png)
or user recieves an error (404)
![Authors_delete_error](./docs/End%20Points/AUTHORS/Authors.delete.error.png)

**Update an author**
- PUT/PATCH
- http://localhost:8080/books/<int:book_id>/authors
- User must be logged in, JSON body data: "first_name", "last_name"
- Response: Author is updated (200)
![Books_update](./docs/End%20Points/AUTHORS/Authors.update.png)
or user recieves an error (404)
![Books_update_error1](./docs/End%20Points/AUTHORS/Authors.update.error.png)

#### GENRES

**View all genres**
- GET
- http://localhost:8080/genres
- User must be logged in
- Response: All authors in database displayed (200)
![Genres_getall](./docs/End%20Points/GENRES/Genres.getall.png)

**View specific genre**
- GET
- http://localhost:8080/genres/<int:genre_id>
- User must be logged in
- Response: Specific genre is displayed (200)
![Genres_getgenre](./docs/End%20Points/GENRES/Genres.getgenre.png)
or user recieves an error (404)
![Genres_getgenre_error](./docs/End%20Points/GENRES/Genres.getgenre.error.png)

**Create a genre**
- POST
- http://localhost:8080/books/<int:book_id>/genres
- User must be logged in, JSON body data: "genre_name"
- Response: Genre is created (200)
![Genres_create](./docs/End%20Points/GENRES/Genres.create.png)
or user recieves an error (404)
![Genres_create_error](./docs/End%20Points/GENRES/Genres.create.error.png)

**Delete a genre**
- DELETE
- http://localhost:8080/genres/<int:genre_id>
- User must be logged in
- Response: Genre is deleted (200)
![Authors_delete](./docs/End%20Points/GENRES/Genres.delete.png)
or user recieves an error (404)
![Authors_delete_error](./docs/End%20Points/GENRES/Genres.delete.error.png)

**Update a genre**
- PUT/PATCH
- http://localhost:8080/books/<int:book_id>/genres
- User must be logged in, JSON body data: "genre_name"
- Response: Genre is updated (200)
![Genres_update](./docs/End%20Points/GENRES/Genres.update.png)
or user recieves an error (400) or (404)
![Genres_update_error1](./docs/End%20Points/GENRES/Genres.update.error1.png)
![Genres_update_error1](./docs/End%20Points/GENRES/Genres.update.error2.png)
