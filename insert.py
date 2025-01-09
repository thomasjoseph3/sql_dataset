import cx_Oracle
from datetime import datetime

# Database connection details
dsn_tns = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
connection = cx_Oracle.connect(user="C##university", password="123", dsn=dsn_tns)
cursor = connection.cursor()

# Data insertion queries
data_insertion_queries = [
    # Insert data into members table
    """
    INSERT INTO members (member_id, first_name, last_name, email, phone, address, join_date, membership_status)
    VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
    """,
    [
        (1, 'John', 'Doe', 'john.doe@example.com', '1234567890', '123 Elm Street', datetime(2022, 5, 15), 'Active'),
        (2, 'Jane', 'Smith', 'jane.smith@example.com', '0987654321', '456 Oak Avenue', datetime(2021, 3, 10), 'Active'),
        (3, 'Alice', 'Brown', 'alice.brown@example.com', '5554443333', '789 Pine Road', datetime(2023, 1, 5), 'Inactive'),
    ],

    # Insert data into books table
    """
    INSERT INTO books (book_id, title, author, genre, publisher, publication_year, isbn, total_copies, available_copies)
    VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
    """,
    [
        (1, 'Python Programming', 'John Doe', 'Programming', 'Tech Books', 2019, '1234567890123', 10, 7),
        (2, 'Data Science Basics', 'Jane Doe', 'Data Science', 'Data Books', 2021, '9876543210987', 5, 2),
        (3, 'Advanced SQL', 'Alice Green', 'Databases', 'DB Books', 2020, '5555555555555', 8, 6),
    ],

    # Insert data into genres table
    """
    INSERT INTO genres (genre_id, genre_name)
    VALUES (:1, :2)
    """,
    [
        (1, 'Programming'),
        (2, 'Data Science'),
        (3, 'Databases'),
    ],

    # Insert data into staff table
    """
    INSERT INTO staff (staff_id, first_name, last_name, email, phone, hire_date, role)
    VALUES (:1, :2, :3, :4, :5, :6, :7)
    """,
    [
        (1, 'Robert', 'Johnson', 'robert.johnson@example.com', '7778889999', datetime(2015, 4, 20), 'Librarian'),
        (2, 'Laura', 'Wilson', 'laura.wilson@example.com', '6667778888', datetime(2018, 7, 25), 'Assistant Librarian'),
    ],

    # Insert data into publishers table
    """
    INSERT INTO publishers (publisher_id, publisher_name, contact_email, contact_phone, address)
    VALUES (:1, :2, :3, :4, :5)
    """,
    [
        (1, 'Tech Books', 'contact@techbooks.com', '1112223333', '123 Tech Way'),
        (2, 'Data Books', 'info@databooks.com', '4445556666', '456 Data Lane'),
    ],

    # Insert data into borrowed_books table
    """
    INSERT INTO borrowed_books (borrow_id, member_id, book_id, borrow_date, due_date, return_date, fine_amount)
    VALUES (:1, :2, :3, :4, :5, :6, :7)
    """,
    [
        (1, 1, 1, datetime(2023, 10, 1), datetime(2023, 10, 15), None, 0),
        (2, 2, 2, datetime(2023, 9, 20), datetime(2023, 10, 5), datetime(2023, 10, 4), 0),
    ],

    # Insert data into reservations table
    """
    INSERT INTO reservations (reservation_id, member_id, book_id, reservation_date, status)
    VALUES (:1, :2, :3, :4, :5)
    """,
    [
        (1, 3, 3, datetime(2023, 11, 1), 'Reserved'),
        (2, 1, 2, datetime(2023, 10, 20), 'Cancelled'),
    ],
]

# Execute data insertion queries
for i in range(0, len(data_insertion_queries), 2):
    query = data_insertion_queries[i]
    data = data_insertion_queries[i + 1]
    try:
        cursor.executemany(query, data)
        print(f"Data inserted into table successfully: {query.split()[2]}")
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"Error inserting data into table: {query.split()[2]} - {error.message}")

# Commit changes
connection.commit()

# Close connection
cursor.close()
connection.close()
