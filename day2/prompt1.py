import ollama 
response = ollama.chat(
    model = "llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"give answers in 2lines."
        },
        {
            "role": "user",
            "content": "explain about tirupati trip?"       
        }
    ]
)
print(response["message"]["content"])