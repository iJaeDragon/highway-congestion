import requests
import cv2
import numpy as np

def read_image_from_url(image_url):
    # URL에서 이미지 다운로드
    response = requests.get(image_url)
    if response.status_code == 200:
        # 이미지를 NumPy 배열로 변환
        image_array = np.frombuffer(response.content, np.uint8)
        # OpenCV에서 사용할 수 있는 이미지로 디코딩
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        return img
    else:
        raise Exception(f"Failed to download image. Status code: {response.status_code}")