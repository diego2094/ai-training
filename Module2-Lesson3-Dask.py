import dask.dataframe as dd

file_path = "employees_large.csv"

df = dd.read_csv(file_path)

filtered_df = df[df['Salary'] > 3000]

grouped_df = filtered_df.groupby('Industry')['Salary'].mean()

result = grouped_df.compute()

result.to_csv("filtered_salary_summary.csv", index=True)

print("Processing complete. Results saved to 'filtered_salary_summary.csv'.")