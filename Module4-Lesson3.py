import openai

sample_text = """
Our company achieved a 20% increase in customer satisfaction in the last quarter by implementing new features in our app.
We also reduced churn rates by 15% and expanded into two new markets, increasing overall revenue by 25%.
"""

basic_prompt = f"Summarize the following text:\n{sample_text}"

structured_prompt = f"Summarize the following text into three concise bullet points:\n{sample_text}"

context_driven_prompt = f"Summarize this report into actionable insights for our team:\n{sample_text}"

client = openai.OpenAI()

def generate_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response.choices[0].message.content.strip()

print("Basic Prompt Response:")
print(generate_response(basic_prompt))

print("\nStructured Prompt Response:")
print(generate_response(structured_prompt))

print("\nContext-Driven Prompt Response:")
print(generate_response(context_driven_prompt))


context = "Alice is a Python Developer in AI Development. Bob is a Data Scientist with Python expertise."
query = "Who is best suited for a Python-related task?"

basic_qa_prompt = f"{query}"

instructional_qa_prompt = f"Use the context below to determine the best person for a Python-related task:\nContext: {context}\n\n{query}"

print("Basic QA Prompt Response:")
print(generate_response(basic_qa_prompt))

contextual_qa_prompt = f"Context: {context}\n\n{query}"

print("\nContextual QA Prompt Response:")
print(generate_response(contextual_qa_prompt))

print("\nInstructional QA Prompt Response:")
print(generate_response(instructional_qa_prompt))

classification_text = "The customer reported an error when uploading files to the application."

basic_classification_prompt = f"Classify the following text:\n{classification_text}"

label_prompt = f"Classify the following text as one of these categories: Technical Issue, Billing Query, or General Inquiry.\n\n{classification_text}"

instructional_classification_prompt = f"Analyze the text below and determine which category it belongs to: Technical Issue, Billing Query, or General Inquiry.\n\nText: {classification_text}"

print("Basic Classification Prompt Response:")
print(generate_response(basic_classification_prompt))

print("\nLabel-Specific Prompt Response:")
print(generate_response(label_prompt))

print("\nInstructional Classification Prompt Response:")
print(generate_response(instructional_classification_prompt))
