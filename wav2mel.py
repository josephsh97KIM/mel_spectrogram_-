#기존 wav로 구성된 sub-URMP 파일을 npy 파일로 변경
import torchaudio
import torchaudio.functional as AF
import torchaudio.transforms as AT
import argparse
import os
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--wav_root', type=str, default='/wav_root')  #wav 지정 위치
parser.add_argument('--save_root', type=str, default='/npy_root') #npy 파일 저장 위치
parser.add_argument('--mode', type=str, default='validation') #train 혹은 validation인지 지정이 
parser.add_argument('--n_fft', type=int, default=512) #512가 가장 좋은 값 , librosa에서는 2048 원래값 256 #다른코드 512
parser.add_argument('--win_length', type=int, default=None) #default가 지정되지 않으면 n_fft
parser.add_argument('--hop_length', type=int, default=160, help='spec.shape[1]=sr/hop_length*dur') #librosa에서는 512로 설정, 코드에서는1024//4 #원래값 80 #다른코드 160
parser.add_argument('--n_mels', type=int, default=80) #80이 가장 좋은 값
parser.add_argument('--fmin', default=125) #transform 코드에서는 125
parser.add_argument('--fmax', default=7600) #transform 코드에서는 7600, 원래값 20000
args = parser.parse_args()
print(args)

#############추가##################
stringsclass ={"viola","oboe","bassoon","flute","tuba","horn","sax","double_bass","cello","trombone","violin","clarinet","trumpet"}
##################################
# for save directory
save_root = os.path.join(args.save_root, args.mode)
if not os.path.isdir(args.save_root):
  os.mkdir(args.save_root)
  os.mkdir(os.path.join(args.save_root, args.mode))
  os.mkdir(save_root)
if not os.path.isdir(os.path.join(args.save_root, args.mode)):
  os.mkdir(os.path.join(args.save_root, args.mode))
  os.mkdir(save_root)
#######추가#############
for y in stringsclass:
    if not os.path.isdir(os.path.join(args.save_root, args.mode, y)):
        os.mkdir(os.path.join(args.save_root, args.mode, y))
        # os.mkdir(save_root)
#########################
if not os.path.isdir(save_root):
  os.mkdir(save_root)

for x in stringsclass:
    wav_root = os.path.join(args.wav_root, args.mode, x)
    labels = os.listdir(wav_root)
    file_paths = []
    for file in labels:
        file_paths.append(os.path.join(wav_root, file))

    cnt=0
    for path in file_paths:
        wav, sr = torchaudio.load(path)
        mel_spectrogram = AT.MelSpectrogram(
            sample_rate=sr,
            n_fft=args.n_fft, 
            win_length=args.win_length, 
            hop_length=args.hop_length, 
            f_min = args.fmin,
            f_max = args.fmax,
            center=True, #웹에서 True가 default
            pad_mode="reflect", #웹에서는 constant 
            power=2.0, #웹에서 2.0이 default 값
            norm='slaney',  #웹에서는slaney에서 사용
            onesided=True, 
            n_mels=args.n_mels, 
            mel_scale='htk'
        )
        melspec = mel_spectrogram(wav)
        filename = os.path.basename(path).split('.')[0]+'_mel.npy'
        save_path = os.path.join(save_root,x,filename)
        cnt+=1
        if cnt%1000==0:
            print(cnt)
        print(save_path)
        if os.path.isfile(save_path):
            continue
        np.save(save_path, melspec)