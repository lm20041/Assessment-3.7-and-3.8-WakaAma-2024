import os
folder  = "waka_ama_db/3.7B resource files/WakaNats2017/"
file = "Final"
points = 0

# List all .lif files in the directory
lif_files = [file for file in os.listdir(folder) if file.endswith(file)]

# Print the full path of each .lif file
for lif_file in lif_files:
    full_path = os.path.join(folder, lif_file)
    print(full_path)