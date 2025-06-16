# 📚 Library Information Management System

A web-based Library Information Management System built with Django. This system allows librarians to manage readers, their registration, and track key information efficiently through a simple and responsive web interface.

---

## 🚀 Features

- 📖 Register new readers with details like name, contact, reference ID, and address
- 🔍 Search and manage registered readers
- 👩‍💼 Admin panel support using Django admin
- 📊 Live reader count displayed on UI
- 🛡️ Input validations and CSRF protection for forms

---

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, Bootstrap (for styling)
- **Database**: SQLite (default Django DB)
- **Admin Interface**: Django admin

---

## 🏗️ Project Structure

```bash
LibraryInformationManagementSystem/
├── db.sqlite3
├── manage.py
├── .gitignore
├── lims_app/                    # Main Django application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── static/                  # Static assets (CSS/JS/images)
│   └── templates/               # HTML templates
├── lims_portal/                # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py

```

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/DivyaBGowda484/LibraryInfoSystem.git
cd LibraryInfoSystem
```
### 2. Create Virtual Environment and Activate
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
If you don’t have requirements.txt, generate it with:

```bash
pip freeze > requirements.txt
```
### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Server
```bash
python manage.py runserver
Visit: http://127.0.0.1:8000
```

### 🔐 Django Admin Access
To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
Login at: http://127.0.0.1:8000/admin
```

### 📌 Screenshots
Add UI screenshots here later.

### 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

### 🙋‍♀️ Author
Divya B Gowda
GitHub: @DivyaBGowda484
