import sqlite3

db_path = "experts_profile.db"

connection = sqlite3.connect(db_path)

cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()

print("Tables in the database:", tables)

table_name = "experts_profile"

cursor.execute(f"PRAGMA table_info({table_name});")

schema = cursor.fetchall()

print(f"Schema of the '{table_name}' table:", schema)

cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")

sample_data = cursor.fetchall()

print(f"Sample data from '{table_name}' table:", sample_data)

connection.close()