import os

lif_directory = "waka_ama_db/3.7B resource files/WakaNats2017/"

# Get a list of all .lif files in the directory
lif_files = [file for file in os.listdir(lif_directory) if file.endswith(".lif")]

# Create a list of lines from all LIF files
keep_lines = []
for file_name in lif_files:
    with open(f"{lif_directory}{file_name}", 'r') as f:
        for line in f:
            line = line.strip()  # Strip leading/trailing whitespace from each line
            keep_lines.append(line)

# Print the lines separated by newline characters
print('\n'.join(keep_lines))