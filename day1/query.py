import ollama 
response = ollama.chat(
    model = "llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "what is ai and how many types of ai applications."       
        }
    ]
)
print(response["message"]["content"])