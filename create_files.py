import os

topics = [
    # "",
    # ""
]

# Starting index
start_index = 1

# Safe relative path
output_dir = os.path.join(os.getcwd(), "10 final projects")

os.makedirs(output_dir, exist_ok=True)

for i, topic in enumerate(topics, start=start_index):
    filename_topic = topic.replace(" ", "_")
    filename = f"{i}_{filename_topic}.py"
    file_path = os.path.join(output_dir, filename)
    open(file_path, 'w').close()
    print(f"Created: {file_path}")
