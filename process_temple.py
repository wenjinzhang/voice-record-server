import os
import shutil

def name_render(array_filename):
    pos_idx = int(array_filename[1][0]) + 1
    if array_filename[2] == 'Fossil':
        device = 'wearable'
    else:
        device = 'VA'
    
    if array_filename[3] == 'TIMIT.mp4':
        command_set = 'T'
    else:
        command_set = 'C'
    
    return "{}/audio/{}/Exp{}_{}.mp4".format(array_filename[0], device, pos_idx, command_set)


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
        array_filename = filename.split('_')
        target = name_render(array_filename)
        target = os.path.join(output_folder, target)
        print(src, target)
        # exit()
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copy2(src, target)
        

        
        