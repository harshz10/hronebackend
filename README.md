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

.
├── main.py # FastAPI app entry point
├── routes/
│ ├── init.py
│ ├── product.py # Product endpoints
│ └── order.py # Order endpoints
├── models/
│ ├── init.py
│ ├── product.py # Pydantic models for Product
│ └── order.py # Pydantic models for Order
├── config/
│ └── db.py # MongoDB client connection
├── .env # Contains sensitive DB credentials
├── .gitignore
├── requirements.txt
├── runtime.txt # Specifies Python version for Render
└── README.md

pgsql
Copy
Edit

---

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

## 🧪 Example Request (Create Product)

POST /products
Content-Type: application/json

{
"name": "Laptop Bag",
"description": "Waterproof laptop bag with compartments",
"price": 1299.99,
"sizes": ["small", "medium", "large"]
}

yaml
Copy
Edit

---

## 🧾 How to Run Locally

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/hronebackend.git
cd hronebackend
2️⃣ Create virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set up .env file
Create a .env file in the root directory:

env
Copy
Edit
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
DB_NAME=your_db_name
5️⃣ Run the server
bash
Copy
Edit
uvicorn main:app --reload
⚙️ Render Deployment Notes
✅ requirements.txt contains all dependencies

✅ runtime.txt set to python-3.10.13

✅ .env variables added securely in Render dashboard

✅ main:app is the entry point (via Uvicorn)

🧠 Author
🔗 Harsh Nagar
