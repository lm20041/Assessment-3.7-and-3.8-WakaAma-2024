lif_file_path ="waka_ama_db/3.7B resource files/WakaNats2017/001-Heat 1-01.lif"
recording_file_path = ["001-Heat 1-01", "002-Heat 1-02","003-Heat 1-03", "004-Heat-01", "005-Heat 1-04", "006-Heat 1-05", "007-Heat-02", "008-Heat 1-06","009-Heat 1-07", "010-Heat 1-08", "011-Heat 1-01", "012-Heat 1-01", "013-Heat 1-02", "014-Heat 1-02", "015-Heat 1-03", "016-Heat 1-03", "017-Heat 1-04", "018-Heat 1-04", "019-Heat 1-05", "020-Bowl Semi-01", "021-Bowl Semi-02", "022-Plate Semi-01", "023-Plate Semi-02", "024-Cup Semi-01", "025-Cup Semi-02", "026-Cup Semi-01", "027-Cup Semi-02", "028-Champ Semi-01", "029-Champ Semi-02", "030-Champ Semi-01", "031-Champ Semi-02", "032-Heat-01", "033-Heat-01", "034-Heat-02", "035-Heat-02", "036-Heat-03", "037-Heat-04", "038-Heat-03", "039-Heat-05", "040-Bowl Final-01", "042-Plate Final-01", "043-Cup Final-01", "044-Cup Final-01", "045-Champ Final-01", "046-Champ Final-01", "047-Heat-01", "048-Heat-01", "049-Heat-02", "050-Heat-02", "051-Heat-03", "052-Heat-04", "053-Heat-03", "054-Heat-05", "055-Semi-01", "056-Heat-06", "057-Semi-02", "058-Heat-01", "059-Heat-02", "060-Heat-01", "061-Heat-03", "062-Heat-04", "063-Heat-02", "064-Heat-05", "065-Heat-06", "066-Heat-03", "067-Heat-07", "068-Heat-01", "069-Heat-01", "070-Heat-02", "071-Heat-03", "072-Heat-02", "073-Heat-04", "074-Cup Semi-01", "075-Heat-05", "076-Cup Semi-02", "077-Heat-06", "078-Champ Semi-01", "079-Heat-07", "080-Champ Semi-02", "081-Semi-01", "082-Semi-02", "083-Semi-01", "084-Final-01", "085-Semi-02", "086-Semi-01", "087-Semi-01", "088-Semi-02", "089-Semi-02", "090-Cup Final-01", "091-Semi-01", "091-Semi-01", "092-Final-01", "093-Semi-02", "094-Champ Final-01", "095-Semi-01", "096-Heat-01", "097-Heat-02", "098-Semi-02", "099-Heat-03", "100-Heat-04", "101-Final-01"]
keep_lines = []
for i in recording_file_path:
  lif_file_path ="waka_ama_db/3.7B resource files/WakaNats2017/"+i+".lif"
  with open(lif_file_path, 'r') as f:
    for line in f:
      line = line.strip()
      keep_lines.append(line)

print('\n'.join(keep_lines))
