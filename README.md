# DevTrack API

## 📌 About Project

This is a simple backend project made using Django REST Framework.
It is used to manage issues (like bugs) and reporters.

---

## 🚀 How to Run

1. Open project folder
2. Install library:

```
pip install djangorestframework
```

3. Run server:

```
python manage.py runserver
```

4. Open in browser:

```
http://127.0.0.1:8000/api/
```

---

## 📡 API

### Reporter

* POST `/api/reporters/` → Add reporter
* GET `/api/reporters/` → Show all reporters
* GET `/api/reporters/?id=1` → Get one reporter

---

### Issue

* POST `/api/issues/` → Add issue
* GET `/api/issues/` → Show all issues
* GET `/api/issues/?id=1` → Get one issue
* GET `/api/issues/?status=open` → Filter issue

---

## 📸 Screenshots




<img width="1920" height="1080" alt="Screenshot (10)" src="https://github.com/user-attachments/assets/96c8122d-4685-44ff-a58d-f2d9d52e32ed" />

<img width="1920" height="1080" alt="Screenshot (9)" src="https://github.com/user-attachments/assets/444fa0f4-b6e1-459c-9eb8-8ab588707a9b" />

<img width="1920" height="1080" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/bd37b36b-174b-43c4-b045-5120b6512c00" />

<img width="1920" height="1080" alt="Screenshot (8)" src="https://github.com/user-attachments/assets/b30bbbdd-8934-462f-afa1-811846f447ff" />

---

## 🧠 Design Decision

I used JSON file instead of database because it is easy and simple for beginners.

---

## ⚙️ Tech Used

* Python
* Django
* Django REST Framework

---

## ✅ Conclusion

This project helps to understand basic API, POST and GET, and simple backend logic.
