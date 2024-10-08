import os
from ultralytics import YOLO
from util import imageProcess

# 현재 파일의 경로 (예: 이 스크립트 파일이 있는 위치)
current_file_path = os.path.abspath(__file__)

# 프로젝트 경로 구하기 (현재 파일의 부모 디렉토리)
project_path = os.path.dirname(os.path.dirname(current_file_path))


# 로컬 YOLOv8 모델 파일 경로
model_path = os.path.join(project_path, 'static\\model', 'best.pt')

def detect(image_path, confidence_threshold=0.5) :
    # YOLOv8 모델 로드
    model = YOLO(model_path)

    # 이미지 읽기
    img = imageProcess.read_image_from_url(image_path)  # 감지할 이미지 경로

    # 객체 감지
    results = model(img)

    # results가 list인 경우 첫 번째 결과에 접근
    if isinstance(results, list) and len(results) > 0:
        detections = results[0].boxes.data  # 각 감지된 객체의 정보 가져오기
    else:
        print("결과가 비어 있거나 예상치 못한 형식입니다.")
        return None

    # 탐지된 객체 필터링 (신뢰도 기준)
    filtered_detections = [det for det in detections if det[-2] >= confidence_threshold]

    # 결과 출력: 탐지된 객체 개수 확인
    num_detections = len(filtered_detections)
    print(f"탐지된 객체 개수: {num_detections}")

    # 각 객체에 대한 정보 출력
    # for det in filtered_detections:
    #     class_id = int(det[5])  # 클래스 ID
    #     confidence = det[-2]  # 신뢰도
    #     bbox = det[:4]  # 바운딩 박스 좌표 (x1, y1, x2, y2)
    #
    #     print(f"클래스 ID: {class_id}, 신뢰도: {confidence:.2f}, 바운딩 박스: {bbox}")

    detectResult = {}
    detectResult["count"] = num_detections

    return detectResult