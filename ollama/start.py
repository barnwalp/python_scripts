import ollama

res = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "What is the purpose of universe and existence?"}
    ],
)
print(res["message"]["content"])
