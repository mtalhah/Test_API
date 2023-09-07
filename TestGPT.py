
import openai

# Set your API key
openai.api_key = "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"

prompt = input("Enter Prompt : ")

# Initialize a conversation
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]

# Send a request
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation
)

creativity=0 #range 0 (deterministic stable) -> 2 (random) 
# Get the assistant's reply
assistant_reply = response['choices'][creativity]['message']['content']
print(assistant_reply)