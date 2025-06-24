# 🍕 Food Delivery App

A responsive and lightweight food ordering platform where users can browse restaurants, view menus, add items to cart, and place orders with delivery and payment details.

---

## 📍 Repository

GitHub Link: [https://github.com/athul-20000/food-delivery-app](https://github.com/athul-20000/food-delivery-app)

---

## ✨ Features

- 🔐 User registration and login
- 🛍️ Add-to-cart system (localStorage based)
- 📋 Cart management and item removal
- 🧾 Checkout with address, phone, and payment method
- 🚫 Login check before placing order
- 📦 Order confirmation with alert
- 💻 Responsive frontend with image backgrounds
- ⚙️ SQLite database with Flask backend

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Database:** SQLite
- **Auth:** Flask session management
- **Deployment Platform:** Render (planned), GitHub

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/athul-20000/food-delivery-app.git
cd food-delivery-app
2. Set Up Virtual Environment
bash
CopyEdit
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
CopyEdit
pip install -r requirements.txt
4. Set Up Database (if schema file exists)
bash
CopyEdit
sqlite3 foodapp.db < schema.sql
Or manually create a foodapp.db with tables: users, restaurants, and menu_items.
5. Run the App
bash
CopyEdit
cd server
python app.py
App runs at: http://localhost:5000
________________________________________
🌍 Deployment Steps (Render)
Deployment will make the site accessible publicly worldwide 
1.	Push your code to GitHub 
2.	Create a Render account
3.	Click New → Web Service
4.	Connect your GitHub repo
5.	Configure:
o	Build Command:
nginx
CopyEdit
pip install -r requirements.txt
o	Start Command:
nginx
CopyEdit
python app.py
6.	Deploy!
7.	Copy the public URL and share it.
________________________________________
📸 Screenshots
Homepage	Menu Page	Cart Page
		
(Replace with actual images or remove this section)
________________________________________
🧪 For Users Opening the Project
If you're trying to run this project locally:
1.	Ensure you have Python 3.x installed
2.	Follow the above setup steps
3.	Navigate to http://localhost:5000 in your browser
4.	Register a user, explore restaurants, and place orders! 🎉
________________________________________
📝 License
This project is built as part of an academic exercise.
Feel free to explore and modify for learning purposes.
________________________________________


