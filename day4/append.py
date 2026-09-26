import ollama

messages = []

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Chat ended.")
        break

    
    messages.append({
        "role": "user",
        "content": question
    })

    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    answer = response["message"]["content"]


    messages.append({
        "role": "assistant",
        "content": answer
    })

    print("\n chat History ")
