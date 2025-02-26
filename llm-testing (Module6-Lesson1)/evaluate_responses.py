import requests
import pandas as pd

API_URL = "http://localhost:8000/api/v1/generate-response"

test_cases = pd.read_csv("test_cases.csv")

results = []
for _, row in test_cases.iterrows():
    query = row["Query"]
    expected_response = row["Expected Response"]

    response = requests.post(API_URL, json={"context": "test","query": query})

    response_text = response.json().get("response", "")

    relevance = 5 if expected_response.lower() in response_text.lower() else 3
    accuracy = 5 if response_text == expected_response else 3
    fluency = 5 if response_text and response_text[0].isupper() and response_text[-1] in ".!?" else 3

    results.append({
        "Query": query,
        "Expected Response": expected_response,
        "Actual Response": response_text,
        "Relevance": relevance,
        "Accuracy": accuracy,
        "Fluency": fluency,
    })

results_df = pd.DataFrame(results)
results_df.to_csv("evaluation_results.csv", index=False)
print("Evaluation complete. Results saved to evaluation_results.csv.")
