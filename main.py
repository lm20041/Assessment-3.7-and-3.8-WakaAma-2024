import requests
from ldrawfile import LDrawFile

# Open the LiF file
lif_file_path = "path/to/your/file.lif"
lif_file = LDrawFile(lif_file_path)

# Access data from the LiF file
print(lif_file.header)
for step in lif_file.steps:
    print(step)