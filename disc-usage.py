import shutil

total, used, free = shutil.disk_usage("/")
usage = (used / total) * 100

if usage > 80:
    print(f"Warning! Disk usage is {usage:.2f}%")
else:
    print(f"Disk usage is normal: {usage:.2f}%")
