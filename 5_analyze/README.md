# analyze

## 분석 범위

### 수도권 내에 영동고속도로 혼잡도를 분석할 예정.

![image](https://github.com/user-attachments/assets/63b2d063-5389-41df-8ba8-ee9925d819da)

## 분석 방법

분석할 영역을 지정하여 해당 범위에 탐지된 자동차 대수를 기준으로 혼잡도를 정하고 해당 구간에 표시한다.
영역 지정은 `ROI`를 사용하였고, 분석하고자 하는 특정 이미지 영역을 정의하는 데 사용한다.

![output_detected_image](https://github.com/user-attachments/assets/1db13492-7716-4885-9275-ad1d8265b710)

범위를 바운딩 박스 형태로 지정했지만, 폴리곤 세그멘테이션 형태로 지정해도 좋을것 같다.

> 테스트 스크립트 : [yolo_detection_roi.zip](https://github.com/user-attachments/files/17265554/yolo_detection_roi.zip)
