import json

def text_to_json(text_lines):
    # Initialize an empty list to store the JSON structure
    json_data = []

    # Initialize variables to keep track of the current topic and subtopic
    current_topic = None
    current_subtopic = None


    for line in text_lines:
        # Remove leading and trailing whitespace from the line
        line = line.strip()
        # Check if the line is empty
        if not line:
            continue
        
        # Check if the line is a topic (e.g., "Topic:")
        if line.endswith(":"):
            current_topic = line[:-1]
            current_subtopic = None
        else:
            # Check if the line is a subtopic (e.g., "   Subtopic:")
            if line.startswith("   "):
                if current_topic:
                    if not current_subtopic:
                        current_subtopic = []
                    current_subtopic.append(line.strip())
            else:
                # Assuming it's a description
                if current_topic:
                    if current_subtopic:
                        current_subtopic.append(line.strip())
                    else:
                        current_topic_description = line.strip()
                        json_data.append({"Topic": current_topic, "Description": current_topic_description})
                else:
                    # If no topic is defined, we can't associate this description, so we skip it.
                    pass

    return json_data

# Example text in the specified format
example_text =''' Topic: Autism Treatment

Description: Autism, or Autism Spectrum Disorder (ASD), is a neurodevelopmental condition that affects social interaction, communication, and behavior. While there is no known cure for autism, various therapies and interventions can help individuals with autism improve their quality of life and develop essential skills.

Subtopics:

Behavioral Therapies
a. Applied Behavior Analysis (ABA)
b. Early Start Denver Model (ESDM)
c. Pivotal Response Treatment (PRT)
d. Floortime (DIR/Floortime)

Speech and Language Therapy
a. Communication Skills Development
b. Augmentative and Alternative Communication (AAC)
c. Social Communication Skills

Occupational Therapy
a. Sensory Integration Therapy
b. Fine Motor Skills Development
c. Self-Care Skills Training

Educational Interventions
a. Individualized Education Program (IEP)
b. Special Education Services
c. Inclusion Programs

Medication Management
a. Medications for Co-occurring Conditions (e.g., anxiety, ADHD)
b. Medications to Manage Challenging Behaviors (in some cases)

Social Skills Training
a. Peer Interaction and Play Skills
b. Emotion Recognition and Expression
c. Social Scripts and Role-Playing

Parent Training and Support
a. Parent Education Programs
b. Coping Strategies for Parents and Caregivers
c. Advocacy and Resources

Sensory Integration Therapies
a. Sensory Diet Development
b. Desensitization Techniques
c. Sensory-Friendly Environments

Assistive Technology
a. Communication Devices and Apps
b. Educational Software
c. Adaptive Tools for Daily Living

Alternative and Complementary Therapies
a. Music Therapy
b. Art Therapy
c. Animal-Assisted Therapy
d. Dietary Interventions (e.g., gluten-free, casein-free diets)

Transition Planning
a. Preparing for Adulthood
b. Vocational Training and Employment Support
c. Independent Living Skills

Applied Behavioral Analysis (ABA) Programs
a. Discrete Trial Training (DTT)
b. Natural Environment Teaching (NET)
c. Positive Behavior Support (PBS)'''

# Convert the example text to JSON
result_json = text_to_json(example_text.split('\n'))

# Pretty-print the JSON result
json_str = json.dumps(result_json, indent=4)
print(json_str)
