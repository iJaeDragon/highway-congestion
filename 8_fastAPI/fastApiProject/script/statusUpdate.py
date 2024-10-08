import os
import json

# 현재 파일의 경로 (예: 이 스크립트 파일이 있는 위치)
current_file_path = os.path.abspath(__file__)

# 프로젝트 경로 구하기 (현재 파일의 부모 디렉토리)
project_path = os.path.dirname(os.path.dirname(current_file_path))
file_path = os.path.join(project_path, 'static', 'map.geojson')  # static/map.json의 절대 경로

# JSON 파일을 불러오는 함수
def load_json():
    with open(file_path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

# JSON 데이터를 저장하는 함수
def save_json(data):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# 특정 ID의 status 수정하는 함수
def update_status(feature_id, new_status):
    # JSON 파일을 불러오기
    json_data = load_json()

    # status 업데이트
    for feature in json_data['features']:
        if feature['properties']['id'] == feature_id:
            feature['properties']['status'] = new_status
            break

    # 수정된 JSON 데이터를 저장하기
    save_json(json_data)
    print("JSON 데이터가 성공적으로 수정되고 저장되었습니다.")