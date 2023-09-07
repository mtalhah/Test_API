import json
import networkx as nx
import matplotlib.pyplot as plt

# Load JSON data from a file
filename = "data.json"  # Replace with your JSON file
with open(filename, "r") as json_file:
    data = json.load(json_file)

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges based on the JSON data
for node in data["nodes"]:
    G.add_node(node["id"], label=node["label"])

for edge in data["edges"]:
    G.add_edge(edge["source"], edge["target"])

# Define node positions (you can customize this)
pos = nx.spring_layout(G)

# Get labels for nodes
node_labels = nx.get_node_attributes(G, "label")

# Draw the graph
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=500, node_color="lightblue", font_size=10, font_color="black")
plt.title("Graph from JSON Data")
plt.show()
