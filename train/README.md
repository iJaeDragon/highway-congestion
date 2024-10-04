# train

## 사전 작업

### ultralytics 패키지 인스톨

`YOLOv8`에서는 `ultralytics` 패키지를 사용하여 훈련을 관리하고 실행하는 방식이 권장된다.

`ultralytics` 패키지는 사용자가 훨씬 쉽게 학습을 진행할 수 있도록 설계되었다.

```
  pip install ultralytics
```

### NVIDIA 드라이버 설치

현재 장착된 GPU와 맞는 드라이버를 설치한다.

> 설치 : https://www.nvidia.com/en-us/drivers/

### CUDA Toolkit 셋업

현재 장착된 GPU와 호환되는 버전으로 설치한다.

테스트는 `CUDA Toolkit` 10.2 버전을 사용하였다.

> 설치 : https://developer.nvidia.com/cuda-10.2-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork

### cuDNN 설치

cuDNN은 CUDA와 함께 PyTorch 및 기타 딥러닝 프레임워크에서 GPU 가속을 지원하는 중요한 라이브러리다.
cuDNN은 NVIDIA의 딥러닝 관련 라이브러리로, CNN(Convolutional Neural Networks)과 같은 신경망을 최적화하여 성능을 개선한다.
PyTorch와 CUDA를 사용할 때 cuDNN을 설치하는 것이 권장한다.

CUDA Tookit 버전과 호환되는 cuDNN 버전을 설치한다.  

> 설치 : https://developer.nvidia.com/cudnn-archive

* 다운로드한 cuDNN ZIP 파일을 추출한다.
* 다음 파일을 CUDA Toolkit의 설치 경로에 복사한다.
  * `bin\cudnn*.dll` → `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\bin`
  * `include\cudnn*.h` → `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\include`
  * `lib\x64\cudnn*.lib` → `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2\lib\x64`

### PyTorch 인스톨

`CUDA Toolkit` 버전에 호환되는 `PyTorch`를 설치한다.

```
pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 torchaudio==0.9.0 --extra-index-url https://download.pytorch.org/whl/cu102
```

## Test

세팅을 완료하고 GPU를 잘 불러오는지 테스트를 해본다.

```
import torch

print(torch.__version__)

print("CUDA Available: ", torch.cuda.is_available())  # True이면 GPU 사용 가능
print("cuDNN Available: ", torch.backends.cudnn.is_available())  # True이면 cuDNN 사용 가능
print("Number of GPUs: ", torch.cuda.device_count())   # 사용 가능한 GPU의 수
if torch.cuda.is_available():
    print("Current Device: ", torch.cuda.current_device())  # 현재 사용 중인 GPU의 ID
    print("Device Name: ", torch.cuda.get_device_name(0))   # 첫 번째 GPU의 이름
```

## data.yaml 설정

data.yaml 폴더 위치를 기준으로 데이터 경로를 지정한다.

```
train: ./images/train
val: ./images/val
nc: 3
names: ['truck', 'bus', 'car']
```

### 실제 구조

```
dataset/
├── images/
│   ├── train/
│   │   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_001.png
│   │   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_002.png
│   │   └── ...
│   ├── val/
│   │   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_001.png
│   │   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_002.png
│   │   └── ...
├── labels/
│   ├── train/
│   │   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_001.txt
│   │   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_002.txt
│   │   └── ...
│   ├── val/
│   │   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_001.txt
│   │   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_002.txt
│   │   └── ...
└── data.yaml  # 데이터셋에 대한 정보
```

## Run train

```
yolo task=detect mode=train data=E:/tp/yolo8/ultralytics-main/ultralytics/data/dataset/data.yaml model=yolov8n.pt epochs=10 imgsz=1920,1080 patience=5 device=0
```
