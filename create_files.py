import os

topics = [
    # "name1 name2" => "name1_name2.py"
]

# Starting index (change this to whatever number you want)
start_index = 5

# Set your target directory
output_dir = r"/9 PyQt5 GUI"

os.makedirs(output_dir, exist_ok=True)

for i, topic in enumerate(topics, start=start_index):
    filename_topic = topic.replace(" ", "_")
    filename = f"{i}_{filename_topic}.py"
    file_path = os.path.join(output_dir, filename)
    open(file_path, 'w').close()
    print(f"Created: {file_path}")
