import pandas as pd
import string


def clean_text(text):
    if pd.isnull(text):
        return ""
    text = text.lower()
    text = text.strip()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def handle_numeric_outliers(column, threshold=1.5):
    q1 = column.quantile(0.25)
    print(q1)
    q3 = column.quantile(0.75)
    print(q3)
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    print(column.clip(lower_bound, upper_bound))
    return column.clip(lower_bound, upper_bound)

file_path = "experts_profile.csv"
df = pd.read_csv(file_path)
df.drop_duplicates(inplace=True)
df['Name'].fillna('unknown name', inplace=True)
df['Partner'].fillna('unknown partner', inplace=True)
df['Technologies'].fillna('unknown technologies', inplace=True)
if 'Salary' in df.columns:
    df['Salary'] = handle_numeric_outliers(df['Salary'])
df['Industry'].fillna('unknown industry', inplace=True)
df['Processed_CV'].fillna('unknown processed CV', inplace=True)
df['Processed_CV_list'].fillna('unknown processed CV list', inplace=True)
text_columns = ['Name', 'Partner', 'Industry']
for column in text_columns:
    df[column] = df[column].apply(clean_text)
output_file_path = "experts_profile_cleaned.csv"
df.to_csv(output_file_path, index=False)
print(f"Cleaned dataset saved to {output_file_path}")