import psutil, platform

print("System:", platform.system(), platform.release())
print("CPU Usage:", psutil.cpu_percent(interval=1))
print("Memory Usage:", psutil.virtual_memory().percent)
print("Disk Usage:", psutil.disk_usage('/').percent)
