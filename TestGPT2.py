import openai
import asyncio

# Set up your API key
openai.api_key = "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"

# Initialize conversation with a system message
conversation = [{"role": "system", "content": "You are a helpful assistant for a netbanking app"}]

async def get_assistant_response(user_input):
    try:
        # Check if the user input contains a script execution command
        if "execute_script" not in user_input.lower():
            # Add user message to the conversation
            conversation.append({"role": "user", "content": user_input})

            print("Generating response... Please wait.")

            # Generate a response with user-defined max tokens
            response = await asyncio.to_thread(openai.ChatCompletion.create,
                                               model="gpt-3.5-turbo",
                                               messages=conversation,
                                               max_tokens=100)  # Set a default max tokens value

            assistant_reply = response['choices'][0]['message']['content']
            print("ASSISTANT:", assistant_reply)

            conversation.append({"role": "assistant", "content": assistant_reply})


    except Exception as e:
        print("An error occurred:", e)

async def main():

    while True:
        user_input = input("YOU: ")

        if user_input.lower() in ["exit", "quit", "bye", "end","thank you"]:
            print("ASSISTANT: Goodbye!")
            break

        await get_assistant_response(user_input)

if __name__ == "__main__":
    asyncio.run(main())
