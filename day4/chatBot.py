import ollama 
msgs = [
    {
        "role":"system",
        "content": "give the answers in simple terms."    }
]
while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    msgs.append(
        {
            "role":"user",
            "content":question
        }
    )
    response = ollama.chat(
        model = "llama3.2:3b",
        messages=msgs
    )
    msgs.append({
        "role":"assistant",
        "content":response["message"]["content"]
    })
    print("AI:",response["message"]["content"])
print("____chat history___\n ")

for msg in msgs:
    if msg["role"] != "system":
    print(msg["role"],":",msg["content"])