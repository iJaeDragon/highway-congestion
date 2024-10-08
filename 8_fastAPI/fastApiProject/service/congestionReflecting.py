import os
import configparser

from script import yoloV8, statusUpdate
from util import jsonUtil, request

# 현재 파일의 경로 (예: 이 스크립트 파일이 있는 위치)
current_file_path = os.path.abspath(__file__)

# 프로젝트 경로 구하기 (현재 파일의 부모 디렉토리)
project_path = os.path.dirname(os.path.dirname(current_file_path))


file_path = os.path.join(project_path, 'static', 'map.geojson')  # static/map.json의 절대 경로


urlProperties = configparser.ConfigParser()
urlProperties.read(os.path.join(project_path, 'propertis', 'url.properties'))

keyProperties = configparser.ConfigParser()
keyProperties.read(os.path.join(project_path, 'propertis', 'key.properties'))

def reflecting() :

    geoInfos = jsonUtil.load_json(file_path)

    for curInfo in geoInfos['features']:
        curProperties = curInfo['properties']
        API_URI = (
                    f'{urlProperties.get("DEFAULT", "its.api.url")}'
                    f'?apiKey={keyProperties.get("DEFAULT", "its.api.key")}'
                    f'&type={curProperties["type"]}' 
                    f'&cctvType={curProperties["cctvType"]}' 
                    f'&minX={curProperties["minX"]}' 
                    f'&maxX={curProperties["maxX"]}' 
                    f'&minY={curProperties["minY"]}' 
                    f'&maxY={curProperties["maxY"]}' 
                    f'&getType={curProperties["getType"]}'
                )

        responseData = request.getRequest(API_URI)

        if responseData is None:
            raise Exception(f"Response Error")
        else :
            detectResult = yoloV8.detect(responseData['response']['data']['cctvurl'])  # 감지 메서드 호출

            curStatus = ""

            if detectResult["count"] < 20:
                curStatus = "1"
            elif 20 <= detectResult["count"] < 30:
                curStatus = "2"
            else:
                curStatus = "3"

            statusUpdate.update_status(curProperties['id'], curStatus)
