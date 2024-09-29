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
```

## 사전 작업

원천데이터를 다운로드 받아 압축을 해제하면 내부 데이터가 `.zip.part` 형태로 분할 압축이 되어 있기 때문에 먼저 병합을 진행해야 한다.

(AI Hub 공식 가이드)

![image](https://github.com/user-attachments/assets/23d3fc95-dcba-4ef7-8847-d7409995a2eb)

`리눅스 OS` 계열에서 진행하길 권장하고 있지만 `윈도우` 환경에서 진행하고 있으므로, `git bash`를 활용 하였다.


```
  # git bash 실행

  cd [분할 압축이 되어 있는 파일 경로로 이동]
  $ cat [파일명].zip.part* > [생성할 파일명].tgz
  # ex) $ cat 1-1.수도권영동선.zip.part* > 1-1.수도권영동선.tgz
  
```
