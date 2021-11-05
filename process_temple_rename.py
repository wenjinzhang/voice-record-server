import os
import shutil

base_folder = './Temple'
output_folder = './Temple_out'

subjects = sorted(os.listdir(base_folder))

for subject in subjects:
    if subject.startswith('.'):
        continue

    sub_folder = os.path.join(base_folder, subject)

    for filename in os.listdir(sub_folder):
        if filename.startswith('.'):
            continue
        src = os.path.join(sub_folder, filename)
        # dist = os.path.join(output_folder, "{}_{}".format(subject,filename))
        if src.find('Default'):
            target = src.replace('Default', '0M')
            os.rename(src, target)
            print("from:", src)
        
        # shutil.copy2(src, dist)