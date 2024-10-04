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
yolo task=detect mode=train data=E:/tp/yolo8/ultralytics-main/ultralytics/data/dataset/data.yaml model=yolov8n.pt epochs=5 imgsz=640 batch=64 patience=3 device=0 --workers=4 --half
```

### 파라미터 의미 

* task=detect:
  * 모델의 작업 유형을 설정합니다. 여기서는 객체 탐지를 수행하기 위해 detect로 설정합니다.

* mode=train:
  * 모드 설정으로, 여기서는 학습 모드를 의미합니다. 모델을 학습시키기 위해 사용됩니다.

* data=E:/tp/yolo8/ultralytics-main/ultralytics/data/dataset/data.yaml:
  * 학습에 사용할 데이터 세트의 경로를 지정합니다. YAML 파일에는 학습 및 검증 데이터 경로, 클래스 수 등이 포함되어 있어야 합니다.\

* model=yolov8n.pt:
  * 사용하려는 사전 훈련된 모델 파일의 경로를 지정합니다. 여기서는 YOLOv8의 작은 버전인 yolov8n.pt를 사용합니다.

* epochs=5:
  * 전체 데이터 세트를 몇 번 반복하여 학습할지를 설정합니다. 이 경우, 모델은 전체 데이터 세트를 5번 학습합니다.
  * 일반적으로 10~100 epoch 사이에서 시작합니다.
  * 복잡한 데이터셋이나 모델의 경우 100 이상의 epoch가 필요할 수 있습니다. 하지만 이 경우 조기 중단(early stopping) 기법을 사용하는 것이 좋습니다.

* imgsz=640:
  * 모델에 입력되는 이미지의 크기를 설정합니다. 640은 640x640 픽셀의 정사각형 이미지를 의미하며, 모델이 이 크기로 이미지를 리사이즈하여 학습합니다.
  * 더 큰 이미지 크기를 사용하면 학습 속도가 느려질 수 있습니다. 이는 각 이미지를 처리하는 데 더 많은 계산이 필요하기 때문입니다. 모델의 훈련 시간이 길어질 수 있으므로, 적절한 배치 크기를 선택해야 합니다.
  * 입력 이미지의 크기를 `640x640`으로 변경할 때, 원본 이미지의 종횡비(aspect ratio)를 무시할 수 있습니다. 이는 특정 객체의 비율이나 위치를 왜곡시킬 수 있습니다. 따라서, 원본 이미지의 비율을 유지하면서 크기를 조정하는 방법을 고려해야 할 수 있습니다.

* batch=64:
  * 학습에 사용될 배치 크기를 설정합니다. 한 번의 업데이트에서 모델이 처리할 이미지의 수입니다. 64는 한 번에 64개의 이미지를 처리하여 가중치를 업데이트한다는 의미입니다.

* patience=3:
  * 조기 종료를 위한 인내 심지어(Early Stopping) 파라미터입니다. 만약 검증 성능이 3 에폭 동안 개선되지 않으면 학습을 조기에 종료합니다.

* device=0:
  * 사용할 장치를 설정합니다. 0은 첫 번째 GPU를 사용하겠다는 의미입니다. 만약 GPU가 없다면 cpu로 변경하여 CPU에서 학습할 수 있습니다.

* --workers=4:
  * 데이터 로딩에 사용할 워커의 수를 설정합니다. 여러 개의 워커를 사용하면 데이터 로딩 속도가 빨라져 학습 효율이 높아집니다.

* --half:
  * 이 플래그를 활성화하면 모델이 16비트 부동 소수점(FP16)으로 학습됩니다. 이렇게 하면 메모리 사용량이 줄어들고, GPU의 성능을 향상시킬 수 있습니다. 그러나 모든 GPU에서 FP16을 지원하지 않을 수 있습니다.


![image](https://github.com/user-attachments/assets/4b6da486-f8ee-4060-a5d2-4f5df0979118)
