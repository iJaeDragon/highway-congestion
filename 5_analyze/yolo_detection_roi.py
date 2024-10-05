import cv2
from ultralytics import YOLO

# 사용자 입력 받기
model_path = input("모델 경로를 입력하세요: ")
image_path = input("이미지 경로를 입력하세요: ")
yolo_box_input = input("YOLO 형태의 영역 크기 (예: 0.571391 0.628193 0.857217 0.743615): ")
result_window_width = int(input("결과 창의 너비를 입력하세요: "))
save_path = input("저장할 경로를 입력하세요 (파일명 포함): ")

# YOLO 정규화된 좌표 입력 처리
yolo_box = list(map(float, yolo_box_input.split()))

# 모델 로드
model = YOLO(model_path)

# 이미지 읽기
image = cv2.imread(image_path)
h, w, _ = image.shape  # 원본 이미지의 높이와 너비

# 정규화된 좌표를 픽셀 좌표로 변환
center_x = int(yolo_box[0] * w)
center_y = int(yolo_box[1] * h)
width = int(yolo_box[2] * w)
height = int(yolo_box[3] * h)

# ROI 좌표 계산
x1 = int(center_x - width / 2)
y1 = int(center_y - height / 2)
x2 = int(center_x + width / 2)
y2 = int(center_y + height / 2)

# 관심 영역 지정
roi = image[y1:y2, x1:x2]

# ROI에 대해 탐지 수행
results = model.predict(roi)

# 결과 시각화
for result in results:
    boxes = result.boxes.xyxy  # 탐지된 박스
    for box in boxes:
        # 텐서를 CPU로 이동하고 NumPy 배열로 변환
        x1_box, y1_box, x2_box, y2_box = box[:4].cpu().numpy().astype(int)

        # ROI 내의 박스 좌표 수정
        x1_box_roi = x1 + x1_box
        y1_box_roi = y1 + y1_box
        x2_box_roi = x1 + x2_box
        y2_box_roi = y1 + y2_box

        # 바운딩 박스 그리기
        cv2.rectangle(image, (x1_box_roi, y1_box_roi), (x2_box_roi, y2_box_roi), (255, 0, 0), 2)

# 관심 영역에 반투명 사각형 그리기
overlay = image.copy()
cv2.rectangle(overlay, (x1, y1), (x2, y2), (0, 255, 0), thickness=cv2.FILLED)  # 초록색으로 채운 사각형
alpha = 0.5  # 투명도 (0.0: 완전 투명, 1.0: 불투명)
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

# 이미지 크기 조정 (비율 유지)
aspect_ratio = h / w
desired_height = int(result_window_width * aspect_ratio)

# 이미지 크기 조정
resized_image = cv2.resize(image, (result_window_width, desired_height))

# 결과 이미지 보여주기
cv2.imshow('Detected Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 결과 이미지 저장
cv2.imwrite(save_path, resized_image)
