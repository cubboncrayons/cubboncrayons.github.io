import json,re,numpy as np,soundfile as sf,onnxruntime as ort
from kokoro_onnx import Kokoro
options=ort.SessionOptions()
options.intra_op_num_threads=2
options.inter_op_num_threads=1
options.enable_cpu_mem_arena=False
session=ort.InferenceSession('kokoro-v1.0.int8.onnx',sess_options=options,providers=['CPUExecutionProvider'])
tts=Kokoro.from_session(session,'voices-v1.0.bin')
text=json.load(open('conversational-transcripts.json'))['en']
clips=[]
for sentence in re.split(r'(?<=[.!?])\s+',text):
 audio,sr=tts.create(sentence,voice='af_heart',speed=.82,lang='en-us')
 clips.extend([audio,np.zeros(4800,dtype=np.float32)])
 print(sentence,round(len(audio)/sr,2),flush=True)
sf.write('conversational-en.wav',np.concatenate(clips),sr,subtype='PCM_16')
print('English complete',flush=True)
