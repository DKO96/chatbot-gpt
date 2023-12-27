from openai import OpenAI

client = OpenAI()

messages = []
system_msg = input("What type of chatbot would you like to create? ")
messages.append({"role": "system", "content": system_msg})

print("Say hello to your new assistant!")
while True:
  user_input = input()  # Changed variable name to avoid conflict with input()
  if user_input == "quit":  # Directly check if the user wants to quit
    break
  messages.append({"role": "user", "content": user_input})
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    max_tokens=50,
    )
    
  reply = response.choices[0].message.content
  messages.append({"role": "assistant", "content": reply})
  print("\n" + reply + "\n")
