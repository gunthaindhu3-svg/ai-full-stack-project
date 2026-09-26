import ollama 
while True:
    question = input("Ask the question: ")
    if question.lower() == "exit":
        break
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
    for message in messages:
        if messages["role"] == "user":
            print("You:", message["content"])
        else:
            print("AI:", message["content"])