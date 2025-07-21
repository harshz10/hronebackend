# 🧠 HROne Backend Task

This is a backend service built using **FastAPI** and **MongoDB** to manage **Products** and **Orders**. It includes full CRUD operations and is deployed on **Render**, with auto-generated Swagger documentation.

---

## 🚀 Live Demo

📌 **Base URL**:  
[https://hronebackend-hesd.onrender.com](https://hronebackend-hesd.onrender.com)

📘 **API Docs (Swagger UI)**:  
[https://hronebackend-hesd.onrender.com/docs](https://hronebackend-hesd.onrender.com/docs)

---

## 🛠️ Tech Stack

- 🔷 FastAPI
- 🍃 MongoDB Atlas (Cloud)
- 🧰 Pydantic for data validation
- 🌐 Uvicorn (ASGI server)
- 📦 Deployed on [Render](https://render.com)

---

## 📁 Folder Structure

```plaintext
backend/
├── main.py                  # FastAPI app entry point
├── routes/
│   ├── __init__.py
│   ├── product.py           # Product API routes
│   └── order.py             # Order API routes
├── models/
│   ├── __init__.py
│   ├── product.py           # Pydantic models for Product
│   └── order.py             # Pydantic models for Order
├── config/
│   └── db.py                # MongoDB connection logic
├── .env                     # MongoDB URI (ignored in git)
├── .gitignore
├── requirements.txt         # Project dependencies
├── runtime.txt              # Python version for Render
└── README.md
```

## 📦 Features

### ✅ Products API

| Method | Endpoint            | Description             |
|--------|---------------------|-------------------------|
| POST   | `/products`         | Create a new product    |
| GET    | `/products`         | Get all products        |
| GET    | `/products/{id}`    | Get single product      |
| PUT    | `/products/{id}`    | Update product          |
| DELETE | `/products/{id}`    | Delete product          |

### ✅ Orders API

| Method | Endpoint            | Description             |
|--------|---------------------|-------------------------|
| POST   | `/orders`           | Create a new order      |
| GET    | `/orders`           | Get all orders          |
| GET    | `/orders/{id}`      | Get single order        |
| PUT    | `/orders/{id}`      | Update order            |
| DELETE | `/orders/{id}`      | Delete order            |

---


### Example Request (Create Product)

```http
POST /products
Content-Type: application/json
```

```json
{
  "name": "Laptop Bag",
  "description": "Waterproof laptop bag with compartments",
  "price": 1299.99,
  "sizes": ["small", "medium", "large"]
}
```


---


---

## 🧾 How to Run Locally

### 1️⃣ Clone the repo
```
git clone https://github.com/your-username/hronebackend.git
cd hronebackend
```

2️⃣ Create Virtual Environment
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Set up .env file
Create a .env file in the root directory:
```
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
DB_NAME=your_db_name
```

5️⃣ Run the server
```
uvicorn main:app --reload
```

⚙️ Render Deployment Notes
✅ requirements.txt contains all dependencies.<br>
✅ runtime.txt set to python-3.10.13. <br>
✅ .env variables added securely in Render Dashboard.<br>
✅ main:app is the entry point (via Uvicorn).<br>


🧠 Author
🔗 Harsh Nagar




