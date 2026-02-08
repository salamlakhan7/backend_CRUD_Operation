
---

# 🏢 Django CRUD – Office Management System

<div align="center">

![Django](https://img.shields.io/badge/Django-5.x-success?style=for-the-badge\&logo=django)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

**A clean and beginner-friendly Django CRUD project focused on real-world fundamentals — not unnecessary complexity.**

[Features](#-features) • [Screenshots](#-screenshots) • [Installation](#-installation) • [Usage](#-usage) • [Project Structure](#-project-structure)

</div>

---

## 🌟 Features

### Core CRUD Functionality

* ➕ **Create Office Records**
* 📋 **Read / List Offices**
* ✏️ **Update Office Information**
* ❌ **Delete with Confirmation**

### Media Handling

* 🖼 **User Image Uploads** using `ImageField`
* 📁 Images stored inside `media/offices/`
* 🧠 Automatic path handling by Django
* 🖥 Images rendered dynamically in templates

### Django Fundamentals

* 📦 App-level `templates` & `static`
* 📝 Django Forms
* 🔐 CSRF protection
* 💬 Django messages framework

---

## 📸 Screenshots

> Screenshots can be added inside a `screenshots/` folder
> and referenced here later.

---

## 🚀 Quick Start

### Prerequisites

* Python **3.10+** (tested on 3.12)
* pip
* Virtual Environment (recommended)

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/salamlakhan7/backend_CRUD_Operation.git
cd backend_CRUD_Operation
```

2. **Create & activate virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install Django**

```bash
pip install django pillow
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Run the server**

```bash
python manage.py runserver
```

6. **Open in browser**

```
http://127.0.0.1:8000/
```

---

## 📖 Usage

### Office Management Flow

1. Add a new office with:

   * Office name
   * Location
   * Number of workers
   * Office image
2. View all offices in a list
3. Update office details
4. Delete office with confirmation popup

---

## 🖼 Media Configuration (Important Part)

### `settings.py`

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Main `urls.py`

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Template Usage

```django
<img src="{{ f.office_image.url }}" alt="{{ f.office_name }}" width="200">
```

📁 Uploaded images are stored automatically in:

```
media/offices/
```

---

## 🛠 Tech Stack

### Backend

* **Django** – Web framework
* **Python 3.12**
* **SQLite3** – Development database

### Frontend

* **HTML (Django Templates)**
* **Basic CSS**

---

## 📁 Project Structure

```
backend_CRUD_Operation/
├── backend_CRUD_Operation/   # Project settings
├── E_rent/                   # Main app
│   ├── templates/
│   ├── static/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── media/
│   └── offices/              # Uploaded images
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🎯 Learning Objectives

This project was built to:

* Master **Django CRUD basics**
* Understand **MEDIA vs STATIC**
* Practice **clean app-level structure**
* Build confidence before complex systems

---

## 👤 Author

**Abdul Salam**
Backend Django Developer
🔗 GitHub: [https://github.com/salamlakhan7](https://github.com/salamlakhan7)

---

## 📝 License

This project is licensed under the **MIT License**.

---

<div align="center">

**Built with Django ❤️**
⭐ Star this repo if it helped your Django journey!

</div>

---


