# 🖥️ System Metrics Dashboard

This is a mini project that visualizes system metrics using a **FastAPI backend** and a **JavaScript/HTML/CSS frontend**.

## 📁 Project Structure

system_metrics/
├── backend/ # FastAPI backend that collects and serves system data
│ ├── main.py
│ ├── metrics.py
│ └── system.json
├── frontend/ # Frontend interface for displaying metrics
│ ├── index.html
│ ├── style.css
│ └── script.js
├── .gitignore
└── README.md


## 🚀 Features

- Collects system metrics (e.g. CPU, memory)
- Serves JSON via a FastAPI endpoint
- Simple, visual frontend dashboard
- Clean and modular architecture

## 🛠️ Technologies Used

- **FastAPI** (Python 3)
- **HTML5**
- **CSS3**
- **JavaScript**

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/system_metrics.git
cd system_metrics

2. Set up and activate a virtual environment (optional but recommended)
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install fastapi uvicorn
4. Run the FastAPI server
bash
Copy
Edit
uvicorn main:app --reload
By default, the server runs at:
http://127.0.0.1:8000

You can test the API at:
http://127.0.0.1:8000/docs – interactive Swagger UI

5. Open the Frontend
In a browser, open:

bash
Copy
Edit
frontend/index.html
Make sure it points to the correct API URL (e.g., http://127.0.0.1:8000/system)

🙌 Credits
Project built by Zsolt Csengeri

📄 License
This project is licensed under the MIT License.






