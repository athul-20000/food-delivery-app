import sqlite3

# Connect to your database
conn = sqlite3.connect('../foodapp.db')
cursor = conn.cursor()

# ✅ Delete all previous restaurants to prevent duplicates
cursor.execute("DELETE FROM restaurants")
conn.commit()

# Sample restaurant data
restaurants = [
    ("Pizza Palace", "New York", "Best pizza in town!"),
    ("Sushi Central", "Tokyo", "Fresh sushi straight from Japan."),
    ("Burger Zone", "Los Angeles", "Juicy burgers with secret sauce."),
    ("Taco Town", "Mexico City", "Authentic Mexican tacos and more."),
    ("Curry Corner", "Delhi", "Delicious North Indian curries.")
]

# Insert restaurants
cursor.executemany("""
    INSERT INTO restaurants (name, location, description)
    VALUES (?, ?, ?)
""", restaurants)

conn.commit()
conn.close()

print("✅ Sample restaurants inserted without duplicates!")


