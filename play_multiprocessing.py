import time
from multiprocessing import Process
from pydub import AudioSegment
from pydub.playback import play
import os
from playsound import playsound

base_folder = './replay_attacker/fangping/'

exps =["voww2", "conw2"]
# load filenames  
folders = os.path.join(base_folder, exps[1])
file_names = sorted(os.listdir(folders))

repeat = 10
start_time = time.time()

def play_process(file_name):
    
    print("------------------------")
    print("now--", (time.time() - start_time))
    print("------------------------")
    song = AudioSegment.from_file(file_name)

    play(song)
    # playsound(file_name)

i = 0
time.sleep(9.5)
for file in file_names:
    # i=i+1
    # if i<3:
    #     continue
    if not file.startswith('.'):
        for i in range(repeat):
            p = Process(target=play_process, args=(os.path.join(folders, file),))
            p.start()
            time.sleep(5)
    
