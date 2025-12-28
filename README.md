# VenusShop

✨ **Modern Django Clothing Store** — a fully functional e-commerce web app built with Django.  
Designed with a clean and modern UI, featuring user authentication, product browsing, cart system, payments, and order management.

## 🚀 Features
- ✅ User registration and login
- 🛍️ Product catalog with add‑to‑cart
- 💳 Stripe payment integration
- 🧾 Order history and management
- 📱 Responsive and user‑friendly interface

## 🧠 Technologies Used
- **Backend:** Python, Django  
- **Frontend:** Django Templates (HTML, CSS, JavaScript)  
- **Database:** SQLite (default)  
- **Payments:** Stripe API

## 📁 Project Structure
venus/
├── cart/ # Shopping cart functionality
├── orders/ # Orders and checkout logic
├── payment/ # Stripe payment integration
├── user/ # User accounts & profiles
├── venus/ # Main site logic & products
├── manage.py
├── requirements.txt
└── README.md

## 🔧 Installation

1. Clone the repo  
```bash
git clone https://github.com/MaRi0NeTka/VenusShop.git
cd VenusShop
```
2.Create and activate a virtual environment
python -m venv env
source env/bin/activate        # Linux / macOS
env\Scripts\activate           # Windows
3.Install dependencies
pip install -r requirements.txt
4.Apply migrations
python manage.py migrate
5.Create a superuser (optional)
python manage.py createsuperuser
6.Run the dev server
python manage.py runserver
