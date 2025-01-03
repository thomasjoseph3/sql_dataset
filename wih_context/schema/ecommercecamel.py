{
    "users": {
        "columns": [
            "userId",
            "username",
            "email",
            "passwordHash",
            "phone",
            "address",
            "joinDate"
        ]
    },
    "products": {
        "columns": [
            "productId",
            "name",
            "description",
            "price",
            "stockQuantity",
            "categoryId"
        ],
        "foreignKeys": {
            "categoryId": "categories"
        }
    },
    "categories": {
        "columns": [
            "categoryId",
            "categoryName",
            "parentCategoryId"
        ],
        "foreignKeys": {
            "parentCategoryId": "categories"
        }
    },
    "orders": {
        "columns": [
            "orderId",
            "userId",
            "orderDate",
            "status",
            "totalPrice"
        ],
        "foreignKeys": {
            "userId": "users"
        }
    },
    "orderItems": {
        "columns": [
            "orderItemId",
            "orderId",
            "productId",
            "quantity",
            "price"
        ],
        "foreignKeys": {
            "orderId": "orders",
            "productId": "products"
        }
    },
    "reviews": {
        "columns": [
            "reviewId",
            "userId",
            "productId",
            "rating",
            "reviewText",
            "reviewDate"
        ],
        "foreignKeys": {
            "userId": "users",
            "productId": "products"
        }
    },
    "coupons": {
        "columns": [
            "couponId",
            "code",
            "discountPercentage",
            "expirationDate",
            "usageLimit"
        ]
    }
}
