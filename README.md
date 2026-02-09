
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

## 🧾 Exam Detail (Mini Project Exam 1)

### 🧾 Django Mini Project Exam Summary (Level 1)

✅ **Exam Title:**
**Local Shops Directory (Mini OLX Style)**

---

### 1️⃣ What I asked you to build (Exam Requirements)

I were required to build a complete Django mini project using:

✅ Topics included

* CRUD (Create, Read, Update, Delete)
* ORM filtering (`rating__gte`, `is_verified=True`)
* Forms (save + update)
* Delete confirmation (POST + `csrf_token`)
* Messages framework
* Static fallback image
* Media upload + display
* Media cleanup:

  * delete old image when updating
  * delete image when deleting record
* Authentication:

  * Signup
  * Login
  * Logout
* Protected pages (`@login_required`)

---

### 2️⃣ What I built (My Answer)

✅ **A) I created a new app**
Instead of mixing everything in one app, I created:

* `E_shop` app

And kept My old work in:

* `E_rent`

This was a professional decision.

---

✅ **B) My model (LocalShop)**

I built:

```python
class LocalShop(models.Model):
    shop_name   = models.CharField(max_length=30)
    city        = models.CharField(max_length=10)
    category    = models.CharField(max_length=10)
    rating      = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    is_verified = models.BooleanField(default=False)
    shop_logo   = models.ImageField(upload_to="shops/", null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
```

⭐ What was perfect here:

* correct field types
* correct `upload_to="shops/"`
* correct validators
* correct timestamps

---

### 3️⃣ My Views (Core Exam Logic)

✅ **Create Shop (Protected)**
I correctly used:

```python
@login_required(login_url="login_view")
```

And correctly handled image upload:

```python
LocalShopForm(request.POST, request.FILES)
```

---

✅ **Shop List (Filter Query)**
I correctly fetched shops:

```python
LocalShop.objects.filter(rating__gte=7, is_verified=True)
```

---

✅ **Delete Shop (Real-world Media Cleanup)**
I correctly implemented:

* delete file from `media/`
* then delete record

```python
if os.path.exists(shop.shop_logo.path):
    os.remove(shop.shop_logo.path)
shop.delete()
```

This is a real-world developer-level skill.

---

✅ **Update Shop (Real-world Media Cleanup)**
I correctly stored old image before update:

```python
old_shop = shop.shop_logo
```

Then after saving, I removed old file if new uploaded:

```python
if "shop_logo" in request.FILES and old_shop:
    if old_shop.path != updated_shop.shop_logo.path:
        os.remove(old_shop.path)
```

This was one of the hardest parts — and I did it.

---

### 4️⃣ Authentication (Phase 2)

✅ **Signup**
 used:

* `UserCreationForm`
* `login(request, user)`

Signup worked.

---

✅ **Login**
 used:

* `AuthenticationForm`
* `form.get_user()`
* `login(request, user)`

Login worked.

---

✅ **Logout**
I made logout view and redirect.

---

### 5️⃣ Templates (MY HTML Logic)

✅ I correctly used:

* `{% csrf_token %}`
* delete confirmation popup
* media display:

```django
<img src="{{ shop.shop_logo.url }}">
```

✅ I also correctly handled fallback static image:

```django
{% if shop.shop_logo %}
    <img src="{{ shop.shop_logo.url }}">
{% else %}
    <img src="{% static 'images/default_office.jpg' %}">
{% endif %}
```

---

### 6️⃣ Problems I faced (Exam mistakes)

These were NOT major logic issues — mostly cleanup issues.

❌ Mistake 1: Wrong messages import
I accidentally wrote:

```python
from pyexpat.errors import messages
```

Correct is:

```python
from django.contrib import messages
```

---

❌ Mistake 2: Unnecessary import
 had:

```python
from streamlit import form
```

Not needed in Django.

---

❌ Mistake 3: Logout message bug
 wrote:

```python
messages.success("you're logout")
```

Correct:

```python
messages.success(request, "You're logged out")
```

---

❌ Mistake 4: URL name mismatch
 template used:

```django
{% url 'logout' %}
```

But My urls had:

```python
name="logout_view"
```

So correct should be:

```django
{% url 'logout_view' %}
```

---

❌ Mistake 5: Signup redirect
I did:

```python
login(request, user)
return redirect("login_view")
```

Better is:

```python
return redirect("shop_list")
```

Because user is already logged in.

---

### 7️⃣ Migration issue (I faced)

I also faced a very real Django problem:

`auto_now_add=True` requires default for old rows

 learned:

* Django needs a value for existing database records
* You must choose option 1 and press enter
* OR use `default=timezone.now`

---

### 8️⃣ My Final Exam Score

First score: **88 / 100**

Then My explained , used a separate app (`E_shop`)
So final score became:

✅ **Final Score: 91 / 100 🔥**

---

### 🏆 Final Conclusion

I proved I can build:

✅ Django CRUD
✅ ORM filtering
✅ Auth system
✅ Real media handling
✅ Media cleanup (update + delete)
✅ multi-app project structure

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

If you want, next I can add **Exam 2 section** later the same way 😄👊🔥
