{
    "users": {
        "columns": [
            "user_id",
            "username",
            "email",
            "password_hash",
            "phone",
            "address",
            "join_date"
        ]
    },
    "products": {
        "columns": [
            "product_id",
            "name",
            "description",
            "price",
            "stock_quantity",
            "category_id"
        ],
        "foreign_keys": {
            "category_id": "categories"
        }
    },
    "categories": {
        "columns": [
            "category_id",
            "category_name",
            "parent_category_id"
        ],
        "foreign_keys": {
            "parent_category_id": "categories"
        }
    },
    "orders": {
        "columns": [
            "order_id",
            "user_id",
            "order_date",
            "status",
            "total_price"
        ],
        "foreign_keys": {
            "user_id": "users"
        }
    },
    "order_items": {
        "columns": [
            "order_item_id",
            "order_id",
            "product_id",
            "quantity",
            "price"
        ],
        "foreign_keys": {
            "order_id": "orders",
            "product_id": "products"
        }
    },
    "reviews": {
        "columns": [
            "review_id",
            "user_id",
            "product_id",
            "rating",
            "review_text",
            "review_date"
        ],
        "foreign_keys": {
            "user_id": "users",
            "product_id": "products"
        }
    },
    "coupons": {
        "columns": [
            "coupon_id",
            "code",
            "discount_percentage",
            "expiration_date",
            "usage_limit"
        ]
    }
}
