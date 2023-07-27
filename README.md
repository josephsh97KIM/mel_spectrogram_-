# mel_spectrogram_
기존 audio 파일 mel_spectrogram파일인 npy파일로 변환하도록 만듬.

## 2022.11 wav2mel.py 파일 생성.  
## 2023.04.07 wav2mel_ESC-50.py 파일 생성.  
기존 ESC-50 meta 데이터 csv로부터 파일을 나누어 저장하게 코드생성.  
## 2023.04.09 wav2mel_FSD.py 파일 생성.   
ESC-50과 같이 meta 데이터 csv로부터 파일을 나누어 저장하지만 label이 두개씩 있는 경우가 있어서 두개 생성 후 각각 해당파일이 들어가도록 생성.
## extract_acav2
- acav100m에서 제공한 20k,200k 크기의 json파일의 경로에 맞춰 youtube로부터 영상을 다운할 수 있는 코드.
