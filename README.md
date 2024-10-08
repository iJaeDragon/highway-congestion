# highway-congestion

> 고속도로 혼잡도 분석 프로젝트

![image](https://github.com/user-attachments/assets/3e0095f8-ebd8-4aab-93ce-2ef7460131c3)

## 목차
* [DataSet](#DataSet)

  * [UseData](#UseData)

* [Model](#Model)

  * [Train](#Train)

  * [Validation](#Validation)
 
  * [Detect](#Detect)
 
* [GIS](#GIS)

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

정확율 평균은 0.777(77.7%)가 나왔으며, 조금의 개선이 필요하다.

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

### Analyze

혼잡도는 Detect 결과중 차량 대수를 기준으로 상태를 처리하며, 기준은 아래와 같이 정의했음.

#### 20대 미만 : 여유

#### 20대 이상 ~ 30대 미만 : 보통

#### 30대 이상 : 혼잡


## GIS

혼잡도 `GIS`를 활용하여 표현 하였으며, `OpenLayers` 라이브러리를 활용 했다.

![image](https://github.com/user-attachments/assets/88d64c1c-687e-496a-a7ec-9be193b4187d)
