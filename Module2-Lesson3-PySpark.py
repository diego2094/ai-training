from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("Large Dataset Processing") \
    .getOrCreate()

file_path = "employees_large.csv"

df = spark.read.csv(file_path, header=True, inferSchema=True)

filtered_df = df.filter(df['Salary'] > 3000)

filtered_df = filtered_df.withColumn("Salary", col("Salary").cast("float"))

grouped_df = filtered_df.groupBy("Industry").avg("Salary")

output_path = "filtered_salary_summary_spark"

grouped_df.write.mode("overwrite").csv(output_path, header=True)


print(f"Processing complete. Results saved to '{output_path}'.")