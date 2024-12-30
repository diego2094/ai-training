import dask.dataframe as dd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

import time

start_time = time.time()

file_path = "experts_profile_large.csv"

df = dd.read_csv(file_path)

filtered_df = df[df['Salary'] > 3000]

grouped_df = filtered_df.groupby('Industry')['Salary'].mean()

result = grouped_df.compute()

result.to_csv("filtered_salary_summary.csv", index=True)

print("Processing complete. Results saved to 'filtered_salary_summary.csv'.")

end_time = time.time()

print(f"Dask Processing Time: {end_time - start_time} seconds")

start_time = time.time()

spark = SparkSession.builder \
    .appName("Large Dataset Processing") \
    .getOrCreate()

file_path = "experts_profile_large.csv"

df = spark.read.csv(file_path, header=True, inferSchema=True)

filtered_df = df.filter(df['Salary'] > 3000)

filtered_df = filtered_df.withColumn("Salary", col("Salary").cast("float"))

grouped_df = filtered_df.groupBy("Industry").avg("Salary")

output_path = "filtered_salary_summary_spark"

grouped_df.write.mode("overwrite").csv(output_path, header=True)


print(f"Processing complete. Results saved to '{output_path}'.")

end_time = time.time()

print(f"PySpark Processing Time: {end_time - start_time} seconds")