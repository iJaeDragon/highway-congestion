import requests

def getRequest(url):
    # GET 요청 보내기
    response = requests.get(url)

    # 응답 확인
    if response.status_code == 200:  # 200 OK 상태 코드 확인
        data = response.json()  # 응답을 JSON으로 변환
        return data
    else:
        raise Exception(f"Failed to Call. Status code: {response.status_code}")

