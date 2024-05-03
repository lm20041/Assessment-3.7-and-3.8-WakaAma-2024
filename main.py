lif_file_path ="waka_ama_db/3.7B resource files/WakaNats2017/001-Heat 1-01.lif"
keep_lines = []
with open(lif_file_path, 'r') as f:
  for line in f:
    line = line.strip()
    keep_lines.append(line)

print('\n'.join(keep_lines))