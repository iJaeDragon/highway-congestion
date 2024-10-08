# highway-congestion

> 고속도로 혼잡도 분석 프로젝트

![image](https://github.com/user-attachments/assets/3e0095f8-ebd8-4aab-93ce-2ef7460131c3)

## 목차
* [DataSet](#DataSet)

  * [UseData](#UseData)

* [Model](#Model)

  * [Train](#Train)

  * [Validation](#Validation)

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

여기에는 섹션 2의 내용이 포함됩니다.
