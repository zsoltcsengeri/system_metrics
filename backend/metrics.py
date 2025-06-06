import psutil
from shutil import disk_usage

# Get CPU usage percentage over 1 second
def get_cpu_usage():
    return {
        "cpu_percentage": psutil.cpu_percent(
            interval=1
        )  # (interval=1) checks cpu usage after 1 sec, otherwise it shows 0
    }

# Get memory usage percentage and used memory in megabytes
def get_memory_details():
    mem = psutil.virtual_memory()
    return {
        "total_mb": round(mem.total / 10024**2, 2),
        "used_mb": round(mem.used / 1024**2, 2),
        "available_mb": round(mem.available / 1024**2, 2),
        "percent": mem.percent,
    }

# Get disk usage percentage and used space in megabytes
def get_disk_details():
    return {
        "disk": round(psutil.disk_usage("/").percent, 2),  # ("/")specify root path
        "used_mb": round(disk_usage("/").used / 1024**2, 2)
    }


print(get_disk_details())
