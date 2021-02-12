from pydub import AudioSegment
from pydub.utils import mediainfo

info = mediainfo("./server_audio/1exp1-1000-1500.wav")
length = int(float(info["duration"])* 1000)
print(length )
