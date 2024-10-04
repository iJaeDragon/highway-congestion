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

### PyTorch 인스톨

`CUDA Toolkit` 버전에 호환되는 `PyTorch`를 설치한다.

```
pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 torchaudio==0.9.0 --extra-index-url https://download.pytorch.org/whl/cu102
```

## Run train

```
yolo task=detect mode=train data=E:/tp/yolo8/ultralytics-main/ultralytics/data/dataset/data.yaml model=yolov8n.pt epochs=10 imgsz=1920,1080 patience=5 device=0
```
