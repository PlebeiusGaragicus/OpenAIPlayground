import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

print("""The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
    Human: Hello, who are you?
    AI: I am an AI created by OpenAI. How can I help you today?""")

while True:
    raw_text = input("Human: ")
    while not raw_text:
        print("Human: ", end="")
        raw_text = input()
    if raw_text == "quit":
        break
    print("AI: ", end="")
    text = start_sequence + raw_text + restart_sequence
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    for i in response["choices"]:
        print(i["text"].strip())

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ",
#   temperature=0.9,
#   max_tokens=150,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0.6,
#   stop=[" Human:", " AI:"]
# )