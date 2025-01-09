import cx_Oracle

# Database connection details
dsn_tns = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
connection = cx_Oracle.connect(user="C##university", password="123", dsn=dsn_tns)
cursor = connection.cursor()

# Drop existing tables
drop_table_queries = [
    "DROP TABLE reservations CASCADE CONSTRAINTS",
    "DROP TABLE borrowed_books CASCADE CONSTRAINTS",
    "DROP TABLE staff CASCADE CONSTRAINTS",
    "DROP TABLE members CASCADE CONSTRAINTS",
    "DROP TABLE books CASCADE CONSTRAINTS",
    "DROP TABLE genres CASCADE CONSTRAINTS",
    "DROP TABLE publishers CASCADE CONSTRAINTS"
]

for query in drop_table_queries:
    try:
        cursor.execute(query)
        print(f"Table dropped successfully: {query.split()[2]}")
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code != 942:  # Ignore table not found error
            print(f"Error dropping table: {query.split()[2]} - {error.message}")

# List of table creation queries in the correct order
table_creation_queries = [
    # Independent tables
    """
    CREATE TABLE members (
        member_id NUMBER PRIMARY KEY,
        first_name VARCHAR2(100),
        last_name VARCHAR2(100),
        email VARCHAR2(100),
        phone VARCHAR2(20),
        address VARCHAR2(255),
        join_date DATE,
        membership_status VARCHAR2(50)
    )
    """,
    """
    CREATE TABLE books (
        book_id NUMBER PRIMARY KEY,
        title VARCHAR2(255),
        author VARCHAR2(100),
        genre VARCHAR2(50),
        publisher VARCHAR2(100),
        publication_year NUMBER,
        isbn VARCHAR2(20),
        total_copies NUMBER,
        available_copies NUMBER
    )
    """,
    """
    CREATE TABLE genres (
        genre_id NUMBER PRIMARY KEY,
        genre_name VARCHAR2(50)
    )
    """,
    """
    CREATE TABLE staff (
        staff_id NUMBER PRIMARY KEY,
        first_name VARCHAR2(100),
        last_name VARCHAR2(100),
        email VARCHAR2(100),
        phone VARCHAR2(20),
        hire_date DATE,
        role VARCHAR2(50)
    )
    """,
    """
    CREATE TABLE publishers (
        publisher_id NUMBER PRIMARY KEY,
        publisher_name VARCHAR2(100),
        contact_email VARCHAR2(100),
        contact_phone VARCHAR2(20),
        address VARCHAR2(255)
    )
    """,
    # Dependent tables
    """
    CREATE TABLE borrowed_books (
        borrow_id NUMBER PRIMARY KEY,
        member_id NUMBER REFERENCES members(member_id),
        book_id NUMBER REFERENCES books(book_id),
        borrow_date DATE,
        due_date DATE,
        return_date DATE,
        fine_amount NUMBER
    )
    """,
    """
    CREATE TABLE reservations (
        reservation_id NUMBER PRIMARY KEY,
        member_id NUMBER REFERENCES members(member_id),
        book_id NUMBER REFERENCES books(book_id),
        reservation_date DATE,
        status VARCHAR2(50)
    )
    """
]

# Execute each query
for query in table_creation_queries:
    try:
        cursor.execute(query)
        print(f"Table created successfully: {query.split()[2]}")
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"Error creating table: {query.split()[2]}")
        print(f"Oracle error code: {error.code}")
        print(f"Oracle error message: {error.message}")

# Close the connection
cursor.close()
connection.close()
