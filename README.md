# 🍔 Food Delivery Web App

This is a simple and interactive food delivery web application built using **Flask**, **SQLite**, **HTML/CSS**, and **JavaScript**. It supports restaurant listings, menus, cart functionality, and user login/registration.

> 🔗 GitHub Repo: [https://github.com/athul-20000/food-delivery-app](https://github.com/athul-20000/food-delivery-app)

---

## 🚀 Features

- 👨‍🍳 Browse restaurants and their menus
- 🛒 Add items to cart (using localStorage)
- 📦 Place orders with address and payment selection
- 🔐 User registration & login
- 💽 SQLite backend for persistent data
- 🎨 Responsive UI with dynamic updates

---

## 🧱 Project Structure

food-delivery-app/
├── client/
│ ├── templates/ # HTML templates (Jinja2)
│ └── static/ # CSS, JS, images
├── server/
│ ├── app.py # Flask backend
│ ├── seed_restaurants.py
│ └── seed_menu_items.py
├── foodapp.db # SQLite database
├── requirements.txt # Python dependencies
├── README.md # Project documentation



## 💻 Running the App Locally

### 🔧 Requirements
- Python 3.x installed
- Flask installed

### 📥 Steps

1. **Clone the repository**  

git clone https://github.com/athul-20000/food-delivery-app.git
cd food-delivery-app


cd food-delivery-app
1. **Install dependencies**  

pip install -r requirements.txt

Run the Flask app

python server/app.py

Open browser and go to:

http://127.0.0.1:5000

🌐 Try on Replit (Free Hosting)
You can also run the app using Replit without deploying permanently.

✅ Steps to Run on Replit:
Create a new Flask Repl at replit.com

Upload your project files:

app.py, templates/, static/, and foodapp.db

Install Flask in the Replit shell:

pip install flask

Set your .replit file to:

run = "python3 app.py"
Click "Run" button
Access your app from the temporary URL Replit provides

⚠️ Replit free URLs expire after ~15 minutes of inactivity

⚠️ Known Limitations
No permanent database (uses local SQLite)

Cart is stored in localStorage (not synced to user account)

Temporary hosting only (unless deployed on a platform like Render/Fly.io)



🧑‍💻 Author
Athul Suseelan, 2025
College of Engineering Trivandrum
athulsuseelan3@gmail.com

📜 License
This project is open-source and free to use for learning and demonstration purposes.

© Athul Suseelan 2025


