import os, re


print ('Building OPlibraries...')

base = os.path.abspath("HGToolkit")
abs_file = os.path.join(base, 'OPlibraries')

for root, dirs, files in os.walk(base):
    for dir in dirs:
        if dir != 'backup':
            for file in os.listdir(os.path.join(base,dir)):
                # for each file in HGT Folders
                if re.match("^.*(hda|hdalc|hdanc)$", file):
                    rel_path = os.path.join(dir, file).replace('\\','/')
                
                    if rel_path not in open(abs_file, "r").read():
                        print("Hit not in file")
                        
                        with open(abs_file, "a") as op_lib:
                            print("Hit write.")
                            op_lib.write('\n'+ rel_path)



print ('Done building OPlibraries...')