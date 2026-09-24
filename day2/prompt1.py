import ollama 
question = input("Ask the question:")
response = ollama.chat(
    model = "llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"give answers in 2lines."
        },
        {
            "role": "user",
            "content": question       
        }
    ]
)
print(response["message"]["content"])