from metrics import get_cpu_usage, get_disk_details, get_memory_details
import json
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so frontend (e.g., HTML/JS in browser) can access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (fine for local dev). In production, restrict this!
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define an API endpoint at /metrics that returns system stats as JSON
@app.get("/metrics")  # ← should start with a forward slash!
async def get_metrics():
    system_data = {
        "CPU": get_cpu_usage(),                     # e.g., {"cpu_percentage": 14.3}
        "MEMORY": get_memory_details(),             # e.g., {"memory_percent": 55.2, "used_mb": 8467.5}
        "DISK": get_disk_details(),                 # e.g., {"disk_percent": 77.1, "used_mb": 125300.7}
        "timestamp": datetime.now().isoformat(),    # Current time for reference
    }

    with open("system.json", "w") as f:
        json.dump(system_data, f, indent=2)

    return system_data
