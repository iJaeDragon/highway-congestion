# highway-congestion

> 고속도로 혼잡도 분석 프로젝트

![image](https://github.com/user-attachments/assets/357c034e-f358-497e-9873-69e3395b07ce)

## 목차
* [Development Environment](#Development-Environment)

  * [Server](#Server)
  
  * [Learning](#Learning)

* [DataSet](#DataSet)

  * [UseData](#UseData)

* [Model](#Model)

  * [Train](#Train)

  * [Validation](#Validation)
 
  * [Detect](#Detect)

* [Analyze](#Analyze)

* [GIS](#GIS)

## Development Environment

### Server

 * Lenguage : Python (3.9.13)
 * Framework : FastAPI
 * Interpreter type : project venv

### Learning

 * Model : YOLOv8
 * Ultralytics 8.3.4
 * CUDA Toolkit 10.2
 * cuDNN
 * PyTorch : 1.9.0+cu102
 * cv2

## DataSet

AI Hub에서 제공하는 교통문제 해결을 위한 `CCTV 교통 영상(고속도로) 데이터셋`을 활용하였다.

![image](https://github.com/user-attachments/assets/43685ff0-e5d3-44af-977a-cace2db4cf53)

### UseData

모든 파일의 총 용량은 1.28 TB 정도 되며, 모든 데이터를 가지고 학습을 진행하는건 어려움이 있어서 `수도권영동선` 데이터만을 사용하였다.

```
100.교통문제 해결을 위한 CCTV 교통 데아터(고속도로)
  - 01.데이터
    - 1.Training
      - 라벨링데이터
        - 바운딩박스
          - 1.수도권영동선.zip|16.13 MB|key:45125
      - 원천데이터
        - 바운딩박스
          - 1-1.수도권영동선.zip|29.84 GB|key: 45139
          - 1-2.수도권영동선.zip|16.81 GB|key: 45140
          - 1-3.수도권영동선.zip|15.17 GB|key: 45141
    - 2.Validation
      - 라벨링데이터
        - 바운딩박스
          - 1.수도권영동선.zip|2.54 MB|key: 45042
      - 원천데이터
        - 바운딩박스
          - 1.수도권영동선.zip|8.99 GB|key: 45056
```

## Model

### Train

|   name   | YOLOv8 model | epoch | batch | imgsz | patience | workers |
|:--------:|:------------:|:-----:|:-----:|:-----:|:--------:|:-------:|
|  first   |     nano     |   5   |  64   |  640  |     3    |    4    |

#### Run

```
yolo task=detect mode=train data=E:/tp/yolo8/ultralytics-main/ultralytics/data/dataset/data.yaml model=yolov8n.pt epochs=5 imgsz=640 batch=64 patience=3 device=0 --workers=4 --half
```

### Validation

![image](https://github.com/user-attachments/assets/afb5665f-56e8-49f9-9465-4bfcba07fd4c)

정확율 평균은 0.429가 나왔으며, 많은 개선이 필요하다.

```
0.30 이하: 성능이 낮은 편으로, 객체 탐지 정확도가 부족하다고 볼 수 있습니다. 간단한 탐지 작업(예: 큰 객체나 단순한 환경)에는 사용할 수 있지만, 정밀한 탐지가 필요한 경우에는 부적합할 수 있습니다.
0.40 ~ 0.50: 중간 정도의 성능으로, 모델이 어느 정도 객체를 탐지하고 위치를 예측할 수 있습니다. 일반적인 CCTV 모니터링, 대량 생산 환경에서의 객체 감지 등 상대적으로 높은 정확도가 요구되지 않는 경우에 적합합니다.
0.50 ~ 0.60: 성능이 양호한 편으로, 실제 응용에서 충분히 사용할 만한 성능입니다. 대부분의 일반적인 객체 탐지 작업에서 잘 작동하며, 실제 산업용, 상업용 애플리케이션에서 활용할 수 있는 수준입니다.
0.60 이상: 높은 성능으로, 모델이 객체의 위치와 경계를 매우 잘 예측할 수 있습니다. 자율 주행, 의료 영상 분석, 보안 시스템 등 정확한 객체 탐지가 필수적인 작업에 적합합니다.
```

`background` 데이터를 학습하지 못해서 다른 데이터를 `background`로 오인식 한 경우가 많으며,<br/>
`bus` 데이터 정확율이 높지 못한 문제가 있다.

![image](https://github.com/user-attachments/assets/71e4abb7-8496-4b54-b552-08f262073062)

![image](https://github.com/user-attachments/assets/6b670c18-d47e-4d23-945d-087aa862a487)

### Detect

![test1](https://github.com/user-attachments/assets/c80f7f80-6667-4675-894a-8fb9cbe7bee0)

#### Detect Result

```
0: 448x640 4 cars, 7.4ms
Speed: 1.0ms preprocess, 7.4ms inference, 1.0ms postprocess per image at shape (1, 3, 448, 640)
```

## Analyze

고속도로를 실시간으로 분석하기 위해서 `국가교통정보센터`에서 제공하는 CCTV 자료를 활용하였다.

![image](https://github.com/user-attachments/assets/458a95aa-41eb-4358-9185-73062950954b)

서버에서 스케줄러를 통해 특정 주기로 구간별로 `Detect`를 수행하여 혼잡도를 파악한다.

혼잡도는 `Detect` 결과중 차량 대수를 기준으로 상태를 처리하며, 기준은 아래와 같이 정의했음.

#### 20대 미만 : 여유

#### 20대 이상 ~ 30대 미만 : 보통

#### 30대 이상 : 혼잡


## GIS

혼잡도는 `GIS`를 활용하여 표현 하였으며, `OpenLayers` 라이브러리를 활용 했다.

![image](https://github.com/user-attachments/assets/88d64c1c-687e-496a-a7ec-9be193b4187d)

### geoJSON

불러온 지도 위에 구간별 혼잡도를 표현하기 위해선 구간별로 좌표를 구해 벡터 선을 그려야 한다.

이때 구간별 좌표를 효율적으로 관리하고 사용하기 위해서 `geoJSON` 데이터 형식을 사용하였다.

#### (영동 고속도로 중 일부 구간 데이터)
```
        
        {
            "type": "Feature",
            "properties": {
                "id": "ED0001",
                "status": "1",
                "type": "ex",
                "cctvType": "3",
                "minX": "126.73660421111015",
                "maxX": "126.74100479368019",
                "minY": "37.4288234275062",
                "maxY": "37.43382986366974",
                "getType": "json"
            },
            "geometry": {
                "coordinates": [
                    [
                        126.73847786616176,
                        37.43291513145789
                    ],
                    [
                        126.73800522194409,
                        37.42963109255997
                    ],
                    [
                        126.73780266013688,
                        37.42808955522875
                    ],
                    [
                        126.73751569757604,
                        37.42579729754779
                    ],
                    [
                        126.7374405876946,
                        37.42435968081777
                    ],
                    [
                        126.73788707164846,
                        37.421032028225085
                    ]
                ],
                "type": "LineString"
            }
        }
```

각 구간을 특정할 수 있도록  `id`를 임의로 지정하였고,  <BR/>
고속도로 영상 자료 호출 API 형식에 맞추기 위해서 CCTV가 존재하는 위,경도 좌표를 미리 입력해놨다. <BR/>

`status` 속성은 혼잡도 상태값이며, 스케줄러에서 분석한 값을 해당 속성에 기록한다.

`1: 여유`, `2: 보통`, `3: 혼잡`

#### CCTV 위치 데이터

```
    {
      "type": "Feature",
      "properties": {
        "id": "C-ED0001",
        "type": "ex",
        "cctvType": "2",
        "minX": "126.73660421111015",
        "maxX": "126.74100479368019",
        "minY": "37.4288234275062",
        "maxY": "37.43382986366974",
        "getType": "json"
      },
      "geometry": {
        "coordinates": [
          126.73847786616176,
          37.43291513145789
        ],
        "type": "Point"
      }
    }
```

해당 위치에 CCTV 아이콘을 추가하여, 클릭 시 영상을 볼 수 있도록 한다.

#### (결과 화면)

![image](https://github.com/user-attachments/assets/6c3dd5fd-2c3e-428b-ac87-9f582745a46f)

초록선은 해당 구간이 여유롭다는 의미이며, 주황선은 보통, 빨간선은 혼잡함을 의미한다.

![image](https://github.com/user-attachments/assets/63a68a08-ea12-48fe-a343-fbb48abb87d8)

CCTV 아이콘을 클릭하여 CCTV 영상을 확인할 수 있다.

## 제언

### 모델 성능

#### 1. 모델 크기 변경

#### 2. 하이퍼 파라미터 상향 조정

#### 3. 백그라운드 데이터 추가

차량 객체가 존재하지 않는 이미지를 찾기는 어려워 인페이팅 AI 도구를 활용하여 차량을 제거하는식으로 이미지를 생성하고 해당 이미지를 백그라운드로 분류하여 학습 시킨다.

![image](https://github.com/user-attachments/assets/492e53c9-f8e4-4f7f-a7a4-dcac1c757a0f)

### 양방향 분석

현재는 이미지에서 방향 상관없이 차량대수를 파악하여 혼잡도를 하나의 선으로 표현하지만, <br/>
방향별로 차량대수를 파악하여, 방향별로 혼잡도를 표현한다.

![image](https://github.com/user-attachments/assets/11b2c5e4-4b0c-439f-945d-9b6858ed104a)
