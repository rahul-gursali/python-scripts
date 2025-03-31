import os
import time

def backup_postgres(db_name, backup_path):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    os.system(f"pg_dump {db_name} > {backup_path}/backup-{timestamp}.sql")

backup_postgres("mydb", "/backups")
