import os
import shutil

base_folder = './Apt'
output_folder = './Apt_one'
subjects = sorted(os.listdir(base_folder))
for subject in subjects:
    if subject.startswith('.'):
        continue
    # subject folder
    sub_folder = os.path.join(base_folder, subject)

    for filename in os.listdir(sub_folder):
        if filename.startswith('.'):
            continue
        src = os.path.join(sub_folder, filename)
        dist = os.path.join(output_folder, "{}_{}".format(subject,filename))
        print("from:", src, "to", dist)
        shutil.copy2(src, dist)

