import openai
import json
import json

def txt2json(filename):
    # Define the input and output file paths
    input_file_path = filename
    output_file_path = "out.json"

    # Read the content of the input text file
    with open(input_file_path, "r") as file:
        text = file.read()

    # Split the text into lines
    lines = text.split('\n')

    # Initialize variables to store the data
    data = {}
    subtopics = []

    # Process each line of the text
    for line in lines:
        # Use regular expressions to extract topic and description
        if line.startswith("Topic: "):
            data["Topic"] = line.replace("Topic: ", "").strip()
        elif line.startswith("Description: "):
            data["Description"] = line.replace("Description: ", "").strip()
        elif line.strip() != "Subtopics:":
            subtopics.append(line.strip())

    # Add the subtopics to the data dictionary
    data["Subtopics"] = subtopics

    # Convert the data to a JSON string
    json_data = json.dumps(data, indent=4)

    # Write the JSON data to a file
    with open(output_file_path, "w") as json_file:
        json_file.write(json_data)

    print(f"JSON data has been generated and written to '{output_file_path}'")


    
def populate_tree(tree, node):
    if isinstance(node, dict):
        for key, value in node.items():
            item = tree.insert("", "end", text=key)
            populate_tree(tree, value)
    elif isinstance(node, list):
        for item in node:
            populate_tree(tree, item)
    else:
        tree.insert("", "end", text=node)


def visualize(filename):
    # Load the JSON data from the file
    with open(filename, "r") as file:
        data = json.load(file)

    # Create the main window
    root = tk.Tk()
    root.title("JSON Tree Visualization")

    # Create a Treeview widget
    tree = ttk.Treeview(root)  # Use ttk from tkinter
    tree.heading("#0", text="JSON Data")
    tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Populate the tree
    populate_tree(tree, data)


# Setup API key
openai.api_key = "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"

# Initialize conversation, setup role of AI
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    # Get user input
    user_input = input("YOU: ")
    # Exit case
    if user_input.lower() in ["exit", "quit", "bye", "end","Thank you"]:
        print("ASSISTANT: Goodbye!")
        break
    user_input = user_input+".Return format:topic: (only the topic name) \n description: (short description for the above)\n subtopics: (only the names in list format) "
    
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

    #write to file
    with open("in.txt","w")as in_file:
        in_file.write(assistant_reply)

    txt2json("in.txt")
    #visualize("out.json")


    
    # Add assistant message to the conversation for context
    conversation.append({"role": "assistant", "content": assistant_reply})





    
