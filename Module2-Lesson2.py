import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

file_path = "employees_cleaned.csv"

df = pd.read_csv(file_path)

print(df.head())

nltk.download('punkt')
nltk.download('punkt_tab')

df['name_tokens'] = df['Name'].apply(word_tokenize)

df['partner_tokens'] = df['Partner'].apply(word_tokenize)

df['industry_tokens'] = df['Industry'].apply(word_tokenize)

print(df[['name_tokens', 'partner_tokens', 'industry_tokens']].head())

output_file_path = "employees_tokenized.csv"

df.to_csv(output_file_path, index=False)

print(f"Tokenized data saved to {output_file_path}")
