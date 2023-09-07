import openai
import json
import json


# Setup API key
openai.api_key = "sk-KR62P4oqxwn9UN00r3aNT3BlbkFJ8W1x7gpWjs0lBRta"

# Initialize conversation, setup role of AI
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    # Get user input
    user_input = input("YOU: ")
    # Exit case
    if user_input.lower() in ["exit", "quit", "bye", "end","Thank you"]:
        print("ASSISTANT: Goodbye!")
        break
    user_input = user_input+".Return format: text inside <> gives context <topic> <description> <subtopics> <description of each subtopic>"
    
    # Add user message to the conversation
    conversation.append({"role": "user", "content": user_input})

    # Indicate that the response is being generated
    print("Generating response...")

    # Send a request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Setup creativity of AI, range (deterministic stable) 0 -> 2 (random)
    creativity = 0

    # Get the assistant's reply
    assistant_reply = response['choices'][creativity]['message']['content']

    print(assistant_reply)
    # Add assistant message to the conversation for context
    conversation.append({"role": "assistant", "content": assistant_reply})





    
