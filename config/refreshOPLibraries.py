import os, re

base = "HGToolkit"

for root, dirs, files in os.walk(base):
    for dir in dirs:
        if dir != 'backup':
            for file in os.listdir(os.path.join(base,dir)):
                #if file.endswith(r'hda|hdalc|hdanc'):
                if re.match("^.*(hda|hdalc|hdanc)$", file):
                    rel_path = os.path.join(dir, file)
                    print(rel_path)
