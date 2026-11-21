import json, os
os.environ['HF_HUB_DISABLE_XET']='1'
os.environ['OMP_NUM_THREADS']='2'
import numpy as np
import soundfile as sf
import torch
torch.set_num_threads(2)
texts={
 'kn':'ನಮಸ್ಕಾರ! ನಿಮ್ಮ ಮಗುವಿನ ಜೊತೆ ಒಂದು ಕಥೆ ಓದೋಣವಾ? ಕಥೆ ಓದ್ತಾ, ಚಿತ್ರ ನೋಡ್ತಾ, ಮಗುವಿಗೆ ಹೇಗಿತ್ತು ಅಂತ ಕೇಳಿ. ಆಮೇಲೆ ಜೊತೆಯಾಗಿ ಒಂದು ಚಿಕ್ಕ ಚಟುವಟಿಕೆ ಮಾಡಿ. ದಿನಕ್ಕೆ ಸ್ವಲ್ಪ ಹೊತ್ತು, ನೀವು ಮತ್ತು ನಿಮ್ಮ ಮಗು. ಬನ್ನಿ, ಒಂದು ಕಥೆ ನೋಡೋಣ!',
 'en':"Got a few minutes with your little one? Let's read a story together. Look at the pictures, ask how they feel, and try a little activity. No rush. Just you, your child, and a little time together. Come on, let's pick a story."
}
with open('conversational-transcripts.json','w',encoding='utf8') as f:json.dump(texts,f,ensure_ascii=False,indent=2)
from ninada import Ninada
import re
tts=Ninada(model_path='ninada-models',lang='kn',voice='female')
clips=[]
for sentence in re.split(r'(?<=[.!?])\s+',texts['kn']):
 tts.reset_filter_state()
 chunks=list(tts.stream(sentence,lang='kn',voice='female',rate=.94,noise=.35,noise_duration=.1,tier='neural'))
 assert all(c['tier']=='neural_onnx' for c in chunks)
 clips.extend([np.concatenate([np.asarray(c['pcm'],dtype=np.float32) for c in chunks]),np.zeros(6000,dtype=np.float32)])
sf.write('conversational-kn.wav',np.concatenate(clips),24000,subtype='PCM_16')
print('Kannada generated',flush=True)
del tts
