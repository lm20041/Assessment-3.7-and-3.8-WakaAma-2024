import os
lif_directory = "waka_ama_db/3.7B resource files/WakaNats2017/"

# Get a list of all .lif files in the directory
lif_files = [file for file in os.listdir(lif_directory) if file.endswith(".lif")]
keep_lines = []
for i in range(5):
  with open(f"{lif_directory}{lif_files[i]}", 'r') as f:
    print(f"Reading {lif_files[i]}")
    for line in f:
      line = line.strip()
      keep_lines.append(line)
    print('\n'.join(keep_lines))
  print('\n\n')
