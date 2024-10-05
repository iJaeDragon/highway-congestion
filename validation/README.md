# Vaildation

최초 train을 진행 할때 Vaildation도 함께 진행이 되지만 <br/>
수동으로 Vaildation을 시작할 수 있다.

## 검증 실행

```
yolo val model=[학습 모델 경로]/best.pt data=[경로]/data.yaml
```
## 검증 완료

### 검증 결과

![image](https://github.com/user-attachments/assets/afb5665f-56e8-49f9-9465-4bfcba07fd4c)

정확율 평균은 0.777(77.7%)가 나왔으며, 조금의 개선이 필요하다.

### confusion_matrix_normalized, confusion_matrix

`Predicted`는 예측한 데이터, `True`는 실제 데이터를 의미한다.<br/>
`background` 데이터를 학습하지 못해서 다른 데이터를 `background`로 오인식 한 경우가 많으며,<br/>
`bus` 데이터 정확율이 높지 못한 문제가 있다.

![confusion_matrix_normalized](https://github.com/user-attachments/assets/caeee858-8a33-4f02-b925-74436cade548)

![confusion_matrix](https://github.com/user-attachments/assets/f322b9c8-c26a-4ea0-90fd-2b382f75410e)
