from fastapi import FastAPI, Query
from datetime import datetime
import socket
import platform
import psutil  # optional (for system stats)

app = FastAPI()

start_time = datetime.now()

@app.get("/health")
def health_check():
    uptime = datetime.now() - start_time
    return {
        "status": "UP",
        "service": "fastapi-app",
        "timestamp": datetime.now().isoformat(),
        "uptime_seconds": int(uptime.total_seconds())
    }


@app.get("/info")
def app_info():
    return {
        "app_name": "FastAPI Demo",
        "host": socket.gethostname(),
        "os": platform.system(),
        "python_version": platform.python_version(),
        "timestamp": datetime.now().isoformat()
    }


@app.get("/time")
def get_time(format: str = Query("iso", enum=["iso", "unix"])):
    now = datetime.now()
    return {
        "format": format,
        "time": now.isoformat() if format == "iso" else int(now.timestamp())
    }


@app.get("/echo")
def echo(message: str):
    return {
        "you_sent": message,
        "length": len(message),
        "timestamp": datetime.now().isoformat()
    }


@app.get("/system")
def system_stats():
    return {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "timestamp": datetime.now().isoformat()
    }