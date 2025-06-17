# 🖥️ System Metrics Dashboard

A mini full-stack project that visualizes system metrics using a **FastAPI backend** and a **JavaScript/HTML/CSS frontend**.

This project demonstrates practical experience with:
- Building and exposing RESTful APIs using Python
- Working with JSON file output
- Frontend API consumption using vanilla JS
- Git-based project structure with modular design

---

## 📁 Project Structure

```
system_metrics/
├── backend/                # FastAPI backend that collects and serves system data
│   ├── main.py             # API entry point
│   ├── metrics.py          # Logic to fetch CPU, memory, and disk stats
│   └── system.json         # Output written on each request
│
├── frontend/               # UI to request and display system metrics
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

---

## 🚀 Features

- 📊 Collects system metrics (CPU, Memory, Disk)
- 🌐 FastAPI endpoint returns JSON-formatted data
- 🎨 Simple frontend dashboard that fetches and displays live data
- 📁 Saves system info to `system.json` for external use (e.g. logging, CSV export)
- 🔄 CORS enabled for frontend-backend communication

---

## 🛠️ Technologies Used

- **FastAPI** (Python 3)
- **psutil** (system metrics collection)
- **HTML5**, **CSS3**, **JavaScript**
- **Git**, virtual environments

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/system_metrics.git
cd system_metrics
```

### 2. Set up and activate a virtual environment

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn psutil
```

### 4. Run the FastAPI server

```bash
uvicorn main:app --reload
```

By default, the server runs at:
- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

### 5. Open the frontend

Open the file `frontend/index.html` directly in your browser.

Make sure the JS fetches from the correct API URL (http://127.0.0.1:8000/metrics).

---

## 🧪 Example API Response

```json
{
  "CPU": { "cpu_percentage": 12.7 },
  "MEMORY": {
    "total_mb": 16234.6,
    "used_mb": 8455.3,
    "available_mb": 7398.8,
    "percent": 52.1
  },
  "DISK": {
    "disk": 71.5,
    "used_mb": 125308.9
  },
  "timestamp": "2025-06-17T22:15:42.379824"
}
```

---

## 🙌 Credits

Project built by **Zsolt Csengeri**

---

## 📄 License

This project is licensed under the MIT License.
