import time
from tqdm import tqdm
from multiprocessing import Process
from pydub import AudioSegment
from pydub.playback import play
import os

def play_process(file_name): 
    song = AudioSegment.from_file(file_name)
    play(song)

base_folder = './replay_attacker/phoneme_segments'
picked_phoneme = ['ae', 'iy', 'ih', 'eh', 'ey', 'aa', 'ay', 'ah', 'ao', 'ow', 'uh',
'uw', 'ux', 'er', 'ax', 'b', 'd', 'p', 't', 'k', 's', 'sh', 'z', 'zh', 'f', 'v', 'm', 
'n', 'ng', 'em', 'nx', 'r', 'w', 'hh', 'hv','dcl','pcl','tcl','kcl','q']

# folders = sorted(os.listdir(base_folder))
folders = picked_phoneme
# print(folders)

start_time = time.time()
time.sleep(10)
pre_time = time.time() - 1

for folder in tqdm(folders):
    if folder.startswith('.'):
        continue

    audio_folder = os.path.join(base_folder, folder)
    audio_file = sorted([filename for filename in os.listdir(audio_folder) if filename.endswith(".wav")])
    
    for i in range(200):
        idx = i % len(audio_file)
        target_audio = os.path.join(audio_folder, audio_file[idx])
        current_time = time.time()
        now = (current_time - start_time)
        runtime = current_time - pre_time
        print(folder, i, target_audio, runtime, now)

        # ready to play audio
        p = Process(target=play_process, args=(target_audio,))
        p.start()
        time.sleep(1)
        pre_time = current_time
        
        



    
