import os

from util import jsonUtil

# 현재 파일의 경로 (예: 이 스크립트 파일이 있는 위치)
current_file_path = os.path.abspath(__file__)

# 프로젝트 경로 구하기 (현재 파일의 부모 디렉토리)
project_path = os.path.dirname(os.path.dirname(current_file_path))
file_path = os.path.join(project_path, 'static', 'map.geojson')  # static/map.json의 절대 경로

# 특정 ID의 status 수정하는 함수
def update_status(feature_id, new_status):
    # JSON 파일을 불러오기
    json_data = jsonUtil.load_json(file_path)

    # status 업데이트
    for feature in json_data['features']:
        if feature['properties']['id'] == feature_id:
            feature['properties']['status'] = new_status
            break

    # 수정된 JSON 데이터를 저장하기
    jsonUtil.save_json(file_path, json_data)
    print("JSON 데이터가 성공적으로 수정되고 저장되었습니다.")