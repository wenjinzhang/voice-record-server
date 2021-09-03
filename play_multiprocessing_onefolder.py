import time
from multiprocessing import Process
from pydub import AudioSegment
from pydub.playback import play
import os
from playsound import playsound

base_folder = './replay_attacker/male/'

# load filenames  
folders = os.path.join(base_folder)
file_names = sorted(os.listdir(folders))
print(file_names)
repeat = 1
start_time = time.time()

def play_process(file_name):
    
    print("------------------------")
    print("now--", (time.time() - start_time))
    print("------------------------")
    song = AudioSegment.from_file(file_name)

    play(song)
    # playsound(file_name)

for file in file_names:
    if not file.startswith('.'):
        for i in range(repeat):
            p = Process(target=play_process, args=(os.path.join(folders, file),))
            p.start()
            time.sleep(10)
    
