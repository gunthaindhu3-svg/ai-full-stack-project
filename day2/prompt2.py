import ollama 
response = ollama.chat(
    model = "llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "I want to plan a trip to tirupati,which we had 5 days and  also go near places tirumala give detailed information that on which date we start wheather traun bus or carand where we stay there what to on time giev me deatiled plan for tirumala?"       
        }
    ]
)
print(response["message"]["content"])