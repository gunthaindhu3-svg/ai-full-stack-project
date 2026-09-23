import ollama 
response = ollama.chat(
    model = "llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "you are a python teacher.what is ai in two line and explain 3 types of ai with 2 examples for each and exaplin clearly how to use"       
        }
    ]
)
print(response["message"]["content"])