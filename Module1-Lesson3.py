import sqlite3

import pandas as pd

import boto3

from botocore.exceptions import NoCredentialsError


def fetch_data_from_db(db_path, query):

    try:

        connection = sqlite3.connect(db_path)

        print("Connected to SQLite database.")

        data = pd.read_sql_query(query, connection)


        connection.close()

        print("Data fetched successfully.")

        return data

    except Exception as e:

        print(f"Error querying the database: {e}")

        return None


def save_data_as_csv(data, file_path):

    try:

        data.to_csv(file_path, index=False)

        print(f"Data saved locally as '{file_path}'.")

    except Exception as e:

        print(f"Error saving data as CSV: {e}")


def upload_to_s3(bucket_name, file_name, s3_key):

    s3 = boto3.client('s3')

    try:

        s3.upload_file(file_name, bucket_name, s3_key)

        print(f"File '{file_name}' uploaded to S3 bucket '{bucket_name}' as '{s3_key}'.")

    except FileNotFoundError:

        print(f"File '{file_name}' not found.")

    except NoCredentialsError:

        print("AWS credentials not found.")

    except Exception as e:

        print(f"Error uploading to S3: {e}")


if __name__ == "__main__":

    db_path = "employees.db"

    query = "SELECT * FROM employees"

    local_csv = "employees.csv"

    bucket_name = "ai-testing-temp"

    s3_key = "ingested_data/employees_data.csv"

    data = fetch_data_from_db(db_path, query)

    if data is not None:

        save_data_as_csv(data, local_csv)
        
        upload_to_s3(bucket_name, local_csv, s3_key)