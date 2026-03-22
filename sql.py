import sqlite3
import pandas as pd

# ─────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────

orders_data = {
    'order_id':       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'customer_name':  ['Rahul Sharma', 'Priya Patel', 'Amit Singh', 'Sneha Rao',
                       'Ravi Kumar', 'Neha Gupta', 'Arjun Mehta', 'Pooja Shah',
                       'Karan Verma', 'Divya Nair'],
    'city':           ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Delhi',
                       'Bangalore', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai'],
    'restaurant':     ['Pizza Hut', "McDonald's", 'Behrouz Biryani', 'Dominos',
                       'KFC', 'Pizza Hut', None, 'Behrouz Biryani', "McDonald's", 'KFC'],
    'cuisine':        ['Italian', 'Fast Food', 'Indian', 'Italian', 'Fast Food',
                       'Italian', 'Indian', 'Indian', 'Fast Food', 'Fast Food'],
    'amount':         [450, 320, None, 600, 280, 530, 410, 390, None, 710],
    'status':         ['delivered', 'cancelled', 'delivered', 'delivered', 'pending',
                       'delivered', 'delivered', 'cancelled', 'pending', 'delivered']
}

customers_data = {
    'customer_id':   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'customer_name': ['Rahul Sharma', 'Priya Patel', 'Amit Singh', 'Sneha Rao',
                      'Ravi Kumar', 'Neha Gupta', 'Arjun Mehta', 'Pooja Shah',
                      'Karan Verma', 'Divya Nair', 'Vikram Malhotra'],
    'email':         ['rahul@gmail.com', 'priya@gmail.com', 'amit@gmail.com',
                      'sneha@gmail.com', 'ravi@gmail.com', 'neha@gmail.com',
                      'arjun@gmail.com', 'pooja@gmail.com', 'karan@gmail.com',
                      'divya@gmail.com', 'vikram@gmail.com']
}

# ─────────────────────────────────────────
#  SETUP DATABASE
# ─────────────────────────────────────────

orders_df    = pd.DataFrame(orders_data)
customers_df = pd.DataFrame(customers_data)

conn = sqlite3.connect("orders.db")
orders_df.to_sql("orders", conn, if_exists="replace", index=False)
customers_df.to_sql("customers", conn, if_exists="replace", index=False)
print(" Database ready! Tables: orders, customers\n")

# ─────────────────────────────────────────
#  WRITE YOUR QUERY HERE ↓
# ─────────────────────────────────────────

query = """
SELECT city, customer_name, amount, Lag(amount) OVER (order by order_id) AS rank FROM orders
"""

# ─────────────────────────────────────────
#  RUN & PRINT
# ─────────────────────────────────────────

result = pd.read_sql_query(query, conn)
print(result.to_string())
conn.close()