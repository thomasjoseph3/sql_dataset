{
    "members": {
        "columns": [
            "member_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "join_date",
            "membership_status"
        ]
    },
    "books": {
        "columns": [
            "book_id",
            "title",
            "author",
            "genre",
            "publisher",
            "publication_year",
            "isbn",
            "total_copies",
            "available_copies"
        ]
    },
    "borrowed_books": {
        "columns": [
            "borrow_id",
            "member_id",
            "book_id",
            "borrow_date",
            "due_date",
            "return_date",
            "fine_amount"
        ],
        "foreign_keys": {
            "member_id": "members",
            "book_id": "books"
        }
    },
    "genres": {
        "columns": [
            "genre_id",
            "genre_name"
        ]
    },
    "staff": {
        "columns": [
            "staff_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "hire_date",
            "role"
        ]
    },
    "reservations": {
        "columns": [
            "reservation_id",
            "member_id",
            "book_id",
            "reservation_date",
            "status"
        ],
        "foreign_keys": {
            "member_id": "members",
            "book_id": "books"
        }
    },
    "publishers": {
        "columns": [
            "publisher_id",
            "publisher_name",
            "contact_email",
            "contact_phone",
            "address"
        ]
    }
}
