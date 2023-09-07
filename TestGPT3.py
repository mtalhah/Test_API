import openai
import json

# Setup API key
openai.api_key = "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"

# Initialize conversation, setup role of AI
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    # Get user input
    user_input = input("YOU: ")
    
    # Exit case
    if user_input.lower() in ["exit", "quit", "bye", "end", "Thank you"]:
        print("ASSISTANT: Goodbye!")
        break
    
    # Prepare user input with a specific format
    user_input = user_input + ".Return format: topic: description: subtopic:"
    
    # Add user message to the conversation
    conversation.append({"role": "user", "content": user_input})

    # Indicate that the response is being generated
    print("Generating response...")

    # Send a request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    
    )

    # Use the first (and only) choice as the response
    assistant_reply = response['choices'][0]['message']['content']

    # Split the assistant's response into separate lines
    response_lines = assistant_reply.split("\n")

    # Create a JSON object with separate keys for "Topic," "Description," and "Subtopic"
    response_json = {}
    current_key = None
    for line in response_lines:
        if ":" in line:
            current_key, current_value = line.split(":", 1)
            current_key = current_key.strip()
            current_value = current_value.strip()
            response_json[current_key] = current_value
        elif current_key:
            response_json[current_key] += "\n" + line.strip()

    # Pretty-print the JSON response
    response_json_str = json.dumps(response_json, indent=4)

    # Print the JSON response
    print("ASSISTANT (JSON):")
    

    # Add assistant message to the conversation for context
    conversation.append({"role": "assistant", "content": response_json_str})


