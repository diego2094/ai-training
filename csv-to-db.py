import csv
import sqlite3

# CSV and SQLite paths
csv_file = 'employees.csv'  # Your CSV file
db_file = 'employees.db'    # SQLite database file

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Read the CSV and create a table in the database
with open(csv_file, 'r', newline='', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)  # Read CSV as dictionaries
    
    # Get the column names and remove the index column (first column)
    columns = csv_reader.fieldnames[1:]  # Skip the first 'index' column
    create_table_query = f"CREATE TABLE IF NOT EXISTS employees ({', '.join([f'{col} TEXT' for col in columns])});"
    cursor.execute(create_table_query)

    # Insert rows into the table
    for row in csv_reader:
        # Skip the index column (first column in CSV)
        row_data = tuple(row[col] for col in columns)
        
        # Prepare the INSERT query with placeholders for values
        placeholders = ', '.join(['?' for _ in columns])  # Use '?' as placeholders
        insert_query = f"INSERT INTO employees ({', '.join(columns)}) VALUES ({placeholders})"
        
        # Execute the insert query
        cursor.execute(insert_query, row_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"CSV data has been successfully inserted into {db_file}")
