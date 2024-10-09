import os
import configparser

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from util import jsonUtil, request
router = APIRouter()

# 현재 파일의 경로 (예: 이 스크립트 파일이 있는 위치)
current_file_path = os.path.abspath(__file__)

# 프로젝트 경로 구하기 (현재 파일의 부모 디렉토리)
project_path = os.path.dirname(os.path.dirname(current_file_path))

file_path = os.path.join(project_path, 'static', 'segmentSection.geojson')  # static/map.json의 절대 경로

urlProperties = configparser.ConfigParser()
urlProperties.read(os.path.join(project_path, 'propertis', 'url.properties'))

keyProperties = configparser.ConfigParser()
keyProperties.read(os.path.join(project_path, 'propertis', 'key.properties'))

@router.post("/cctv/getCctv")
async def getCctv(propertis: dict = Body(...)):

    API_URI = (
        f'{urlProperties.get("DEFAULT", "its.api.url")}'
        f'?apiKey={keyProperties.get("DEFAULT", "its.api.key")}'
        f'&type={propertis["type"]}'
        f'&cctvType={propertis["cctvType"]}'
        f'&minX={propertis["minX"]}'
        f'&maxX={propertis["maxX"]}'
        f'&minY={propertis["minY"]}'
        f'&maxY={propertis["maxY"]}'
        f'&getType={propertis["getType"]}'
    )

    responseData = request.getRequest(API_URI)

    return JSONResponse(responseData)