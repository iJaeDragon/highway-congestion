# highway-congestion

> 고속도로 혼잡도 분석 프로젝트

![image](https://github.com/user-attachments/assets/3e0095f8-ebd8-4aab-93ce-2ef7460131c3)

## 목차
* [DataSet](#DataSet)

  * [UseData](#UseData)

* [Model](#Model)

  * [Train](#Train)

  * [Validation](#Validation)
   
    * [confusion_matrix_normalized, confusion_matrix](#confusion_matrix_normalized,-confusion_matrix)

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

여기에는 섹션 1의 내용이 포함됩니다.

### Validation

![image](https://github.com/user-attachments/assets/afb5665f-56e8-49f9-9465-4bfcba07fd4c)

정확율 평균은 0.777(77.7%)가 나왔으며, 조금의 개선이 필요하다.

### confusion_matrix_normalized, confusion_matrix

`background` 데이터를 학습하지 못해서 다른 데이터를 `background`로 오인식 한 경우가 많으며,<br/>
`bus` 데이터 정확율이 높지 못한 문제가 있다.

![confusion_matrix_normalized](https://github.com/user-attachments/assets/caeee858-8a33-4f02-b925-74436cade548)

![confusion_matrix](https://github.com/user-attachments/assets/f322b9c8-c26a-4ea0-90fd-2b382f75410e)

