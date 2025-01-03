{
    "members": {
        "columns": [
            "memberId",
            "firstName",
            "lastName",
            "email",
            "phone",
            "address",
            "joinDate",
            "membershipStatus"
        ]
    },
    "books": {
        "columns": [
            "bookId",
            "title",
            "author",
            "genre",
            "publisher",
            "publicationYear",
            "isbn",
            "totalCopies",
            "availableCopies"
        ]
    },
    "borrowedBooks": {
        "columns": [
            "borrowId",
            "memberId",
            "bookId",
            "borrowDate",
            "dueDate",
            "returnDate",
            "fineAmount"
        ],
        "foreignKeys": {
            "memberId": "members",
            "bookId": "books"
        }
    },
    "genres": {
        "columns": [
            "genreId",
            "genreName"
        ]
    },
    "staff": {
        "columns": [
            "staffId",
            "firstName",
            "lastName",
            "email",
            "phone",
            "hireDate",
            "role"
        ]
    },
    "reservations": {
        "columns": [
            "reservationId",
            "memberId",
            "bookId",
            "reservationDate",
            "status"
        ],
        "foreignKeys": {
            "memberId": "members",
            "bookId": "books"
        }
    },
    "publishers": {
        "columns": [
            "publisherId",
            "publisherName",
            "contactEmail",
            "contactPhone",
            "address"
        ]
    }
}
