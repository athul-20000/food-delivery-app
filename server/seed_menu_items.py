import sqlite3

# Connect to your database
conn = sqlite3.connect('../foodapp.db')
cursor = conn.cursor()

# ✅ Delete existing menu items to avoid duplicates
cursor.execute("DELETE FROM menu_items")
conn.commit()

# 🔍 Fetch restaurant IDs by name to avoid hardcoding
cursor.execute("SELECT id, name FROM restaurants")
restaurant_map = {name: id for id, name in cursor.fetchall()}

# Sample menu items mapped to restaurant name
menu_items = [
    # Pizza Palace
    (restaurant_map['Pizza Palace'], "Margherita Pizza", "Classic cheese and tomato pizza", 299.00, "https://i.pinimg.com/736x/18/37/f7/1837f7b2e6cc429f44a7d3dec38bccd9.jpg"),
    (restaurant_map['Pizza Palace'], "Pepperoni Pizza", "Loaded with pepperoni slices", 349.00, "https://www.hunts.com/sites/g/files/qyyrlu211/files/uploadedImages/img_6934_48664.jpg"),

    # Sushi Central
    (restaurant_map['Sushi Central'], "Salmon Roll", "Fresh salmon with avocado", 450.00, "https://cdn.urbancookery.com/2021/01/ceviche_2.jpg__900x1100_q85_crop.jpg"),
    (restaurant_map['Sushi Central'], "Tuna Nigiri", "Slices of tuna over rice", 420.00, "https://www.simplyrecipes.com/thmb/uOOGnoA0Vmzbk3mOtJK6eYOOgu4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/simply-recipes-spicy-tuna-rice-bowl-lead-1-cc5960e3dd6241479c2d36f57a7b3e14.jpg"),

    # Burger Zone
    (restaurant_map['Burger Zone'], "Cheeseburger", "Juicy beef patty with cheese", 199.00, "https://cdn.pixabay.com/photo/2014/10/23/18/05/burger-500054_960_720.jpg"),
    (restaurant_map['Burger Zone'], "Veggie Burger", "Grilled veggie patty", 179.00, "https://www.eatingwell.com/thmb/bKG34-yS8FjpBQH77B1pXgsjcms=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/EW-Zucchini-Chickpea-Veggie-Burgers-with-Tahini-Ranch-Sauce-1x1-c6d1c8e20e3144bf95063134a4a518a8.jpg"),

    # Taco Town
    (restaurant_map['Taco Town'], "Beef Taco", "Minced beef with salsa", 159.00, "https://cdn.pixabay.com/photo/2014/10/23/18/05/taco-500054_960_720.jpg"),
    (restaurant_map['Taco Town'], "Chicken Quesadilla", "Spiced chicken in melted cheese", 199.00, "https://www.julieseatsandtreats.com/wp-content/uploads/2024/10/Chicken-Quesadilla-Square.jpg"),

    # Curry Corner
    (restaurant_map['Curry Corner'], "Butter Chicken", "Creamy tomato gravy with chicken", 299.00, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTY53Zww8_j72B0sOb6m4o4fOMO0eDtsvvwQ&s"),
    (restaurant_map['Curry Corner'], "Paneer Tikka Masala", "Spicy paneer curry", 279.00, "https://www.cookwithmanali.com/wp-content/uploads/2014/04/Paneer-Tikka-Masala.jpg")
]

# Insert into menu_items table
cursor.executemany("""
    INSERT INTO menu_items (restaurant_id, name, description, price, image_url)
    VALUES (?, ?, ?, ?, ?)
""", menu_items)

conn.commit()
conn.close()

print("✅ Sample menu items inserted without duplicates or ID mismatch!")

