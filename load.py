import sqlite3
 
def load(data):
    print("\nLoading data into database...")
 
    conn = sqlite3.connect("zomato.db")
    data.to_sql("restaurants", conn, if_exists="replace", index=False)
 
    print("Data loaded successfully!")
    print(f"Table: restaurants")
    print(f"Rows loaded: {len(data)}")
 
    conn.close()
 