# 📚 Library Information Management System

A comprehensive web-based Library Information Management System built with Django. This system provides complete library operations including reader management, book catalog, borrowing/lending, returns processing, and inventory tracking through an intuitive web interface.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

---

## 🚀 Features

### 👥 Reader Management
- 📝 Register new readers with complete details (name, contact, reference ID, address)
- 🔍 Search and filter registered readers
- ✏️ Edit and manage reader information
- 📊 Track active/inactive readers

### 📚 Book Management
- 📖 Add books with ISBN, title, author, genre, publication year
- 🔍 Search books by title, author, or genre
- 📊 Track total copies and available copies
- 📈 Real-time inventory management

### 🛍️ Borrowing System
- 📋 Browse complete book collection
- 🛒 Borrow books with reader selection
- ⏰ Automatic due date calculation (14-day period)
- 🔒 Availability checking and validation

### 🎒 My Bag (Borrowed Books)
- 📱 View all currently borrowed books
- 👤 Filter by specific readers
- ⚠️ Visual overdue indicators
- 📅 Days remaining/overdue calculations
- 📊 Comprehensive borrowing statistics

### 🔄 Returns Processing
- 📦 Process book returns with confirmation dialogs
- ⏰ Overdue book tracking and notifications
- 📞 Reader contact information for follow-ups
- 📊 Return statistics and analytics
- 🔄 Automatic inventory updates

### 🛡️ Admin Interface
- 👨‍💼 Enhanced Django admin with custom forms
- 🎯 Bulk actions for processing returns
- 📋 Advanced filtering and search capabilities
- 📊 Overdue status tracking
- ✅ Form validation and error handling

### 🎨 User Experience
- 📱 Responsive Bootstrap design
- 🧭 Intuitive navigation between all sections
- 💬 Success/error message notifications
- 🎯 Modal dialogs for confirmations
- 📊 Real-time status indicators

---

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Django 5.x
- **Frontend**: HTML5, CSS3, Bootstrap 5.3
- **Database**: SQLite (default) / PostgreSQL ready
- **Admin Interface**: Enhanced Django Admin
- **Authentication**: Django built-in auth system
- **Forms**: Django Forms with CSRF protection

---

## 🎥 Demo

[![Watch the demo](https://img.youtube.com/vi/BIIp7xqaD6w/0.jpg)](https://youtu.be/BIIp7xqaD6w)

*Click the image above to watch a full demo of the system in action!*


---

## 🏗️ Project Structure

```bash
LibraryInformationManagementSystem/
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore patterns
├── lims_app/                  # Main Django application
│   ├── __init__.py
│   ├── admin.py              # Enhanced admin interface
│   ├── apps.py
│   ├── models.py             # Reader, Book, BorrowedBook models
│   ├── views.py              # All view functions
│   ├── urls.py               # URL routing
│   ├── tests.py
│   ├── migrations/           # Database migrations
│   │   ├── 0001_initial.py
│   │   └── 0002_book_borrowedbook.py
│   ├── static/               # Static assets
│   │   └── LIMS_LOGO_BIG.png
│   └── templates/            # HTML templates
│       ├── index.html        # Base template with navigation
│       ├── home.html         # Welcome page
│       ├── readers.html      # Reader management
│       ├── books.html        # Book catalog and borrowing
│       ├── my_bag.html       # Borrowed books tracking
│       ├── returns.html      # Returns processing
│       └── welcome.html      # Success pages
├── lims_portal/              # Django project configuration
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
```

---

## ⚙️ Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- Git

### 2. Clone the Repository
```bash
git clone https://github.com/DivyaBGowda484/LibraryInformationManagementSystem.git
cd LibraryInformationManagementSystem
```

### 3. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install django
# Or if you have requirements.txt:
pip install -r requirements.txt
```

### 5. Database Setup
```bash
# Run migrations to set up the database
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Admin User
```bash
python manage.py createsuperuser
# Follow prompts to create admin credentials
```

### 7. Start the Development Server
```bash
python manage.py runserver
```

### 8. Access the Application
- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## 📱 Application Pages

| Page | URL | Description |
|------|-----|-------------|
| **Home** | `/` | Welcome page with library information |
| **Readers** | `/readers` | Manage library readers |
| **Books** | `/books` | Browse and borrow books |
| **My Bag** | `/my_bag` | View borrowed books |
| **Returns** | `/returns` | Process book returns |
| **Admin** | `/admin/` | Enhanced admin interface |

---

## 🎯 Key Functionalities

### For Librarians:
1. **Register new readers** with complete information
2. **Add books** to the library catalog with inventory tracking
3. **Process borrowing** with automatic due date setting
4. **Track borrowed books** with overdue notifications
5. **Handle returns** with inventory updates
6. **Generate reports** through admin interface

### For System Administration:
1. **Bulk operations** through admin interface
2. **Advanced filtering** and search capabilities
3. **Inventory management** with real-time updates
4. **User management** and permissions
5. **Data validation** and error handling

---

## 🔐 Admin Interface Features

- **Enhanced Forms**: Custom forms with validation and help text
- **Bulk Actions**: Process multiple returns simultaneously
- **Advanced Filtering**: Filter by return status, dates, overdue books
- **Search Functionality**: Search across readers, books, and transactions
- **Status Indicators**: Visual indicators for overdue books
- **Inventory Tracking**: Automatic updates when books are borrowed/returned

---

## 🚧 Future Enhancements

- [ ] Email notifications for overdue books
- [ ] Book reservation system
- [ ] Advanced reporting and analytics
- [ ] Mobile app integration
- [ ] Barcode scanning support
- [ ] Fine calculation system
- [ ] Book recommendation engine
- [ ] Multi-library support

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
