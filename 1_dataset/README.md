# DataSet

![image](https://github.com/user-attachments/assets/672cff16-a4ee-4f47-85d8-60cfa9f7b8a7)

AI Hub에서 `제공하는 교통문제 해결을 위한 CCTV 교통 영상(고속도로)` 데이터셋을 활용하였다.

URL : https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=164

## 사용한 파일 목록

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

## 원천데이터

### 사전 작업

원천데이터를 다운로드 받아 압축을 해제하면 내부 데이터가 `.zip.part` 형태로 분할 압축이 되어 있기 때문에 먼저 병합을 진행해야 한다.

```
최초 .tar -> 압축해제 .zip.part -> 병합 .tar -> 압축해제 -> 최종 .wav
```


(AI Hub 공식 가이드)

![image](https://github.com/user-attachments/assets/23d3fc95-dcba-4ef7-8847-d7409995a2eb)

`리눅스 OS` 계열에서 진행하길 권장하고 있다. <br/>
`윈도우` 환경에서 진행하려고 시도 하였지만 방법을 찾지 못했기 때문에  `리눅스 OS` 에서 진행 하였다.

#### 1. .zip.part 파일을 리눅스로 옮김.

![image](https://github.com/user-attachments/assets/6f2b1cd9-242a-4e41-be41-f6cb658c3835)


#### 2. 파일 병합 진행
```
  find "[폴더경로]" -name "[파일명].zip.part*" -print0 | sort -zt'.' -k2V | xargs -0 cat > "[파일명].zip"

  # ex)

  # find "/ds/download2/100.교통문제_해결을_위한_CCTV_교통_데이터(고속도로)/01.데이터/1.Training/원천데이터/바운딩박스/" -name "1-3.수도권영동선.zip.part*" -print0 | sort -zt'.' -k2V | xargs -0 cat > "1-3.수도권영동선.zip"
  # find "/ds/download1/100.교통문제_해결을_위한_CCTV_교통_데이터(고속도로)/01.데이터/1.Training/원천데이터/바운딩박스/" -name "1-2.수도권영동선.zip.part*" -print0 | sort -zt'.' -k2V | xargs -0 cat > "1-2.수도권영동선.zip"
  # find "/ds/download/100.교통문제_해결을_위한_CCTV_교통_데이터(고속도로)/01.데이터/1.Training/원천데이터/바운딩박스/" -name "1-1.수도권영동선.zip.part*" -print0 | sort -zt'.' -k2V | xargs -0 cat > "1-1.수도권영동선.zip"
```

#### 3. 병합된 .zip 파일 압축해제

![image](https://github.com/user-attachments/assets/a51f647e-9ace-47ca-a84c-90c4e458037a)


![image](https://github.com/user-attachments/assets/a59d5726-62df-4e99-bd9d-039a5abcd6ce)


## 라벨링데이터

### 사전 작업

가장 먼저 압축을 해제하고 파일을 보면 `.xml` 형태이다. <br/>
이는 `YOLO`에서 사용할 수 없는 포맷이므로, `YOLO`에서 사용 가능한 포맷으로 수정하여야 한다.

아래 구조처럼 label과 image가 1:1 매치가 되어야 하고 기존 데이터셋은 하나의 xml 파일에서 여러개의 이미지를 지정하여 설정이 되어 있기 떄문에 <br/>
기존 xml파일을 기반으로 YOLO 모델 학습에 적합한 구조를 구성하기 위해서 스크립트를 작성하였다.

```
dataset/
├── images/
│   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_001.png
│   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_002.png
│   └── ...
├── labels/
│   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_001.txt
│   ├── Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD_002.txt
│   └── ...
└── data.yaml  # 데이터셋에 대한 정보
```

(XML TO YOLO Script)
[0_script.zip](https://github.com/user-attachments/files/17210796/0_script.zip)

해당 스크립트를 사용하여 포맷을 변경하였다.


#### xml_to_yolo_multiple.py

디렉터리를 설정하여 모든 파일을 한번에 변경해 주는 스크립트

```
  py xml_to_yolo_multiple.py
  XML 파일이 있는 디렉토리를 입력하세요: [.xml 파일이 있는 디렉터리 입력]
  저장할 디렉토리를 입력하세요: [포맷을 변경한 파일을 저장할 디렉터리 입력]
```

#### xml_to_yolo_single.py

특정 파일을 설정하여 해당 파일을 변경해 주는 스크립트

```
  py xml_to_yolo_single.py
  XML 파일 경로를 입력하세요: [특정 .xml 파일 디렉터리 입력]
  저장할 디렉토리를 입력하세요: [포맷을 변경한 파일을 저장할 디렉터리 입력]
```
#### 변환 완료

![image](https://github.com/user-attachments/assets/7f9bfb52-1370-445c-a7c8-7cac159d473d)

