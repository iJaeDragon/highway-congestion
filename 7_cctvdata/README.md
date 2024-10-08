# CCTV DATA

> 실시간 CCTV 관련 데이터는 국가교통정보센터에서 제공하는 오픈API를 사용하였다. <br/>
> (사용하기 위해서는 인증키 발급 신청을 해야되며, 1~2일 정도 소요됨) <br/>
> URL : https://www.its.go.kr/

## 호출 형식

```
  'https://openapi.its.go.kr:9443/cctvInfo' +
  '?apiKey=[발급받은 인증키]' +
  '&type=[도로 유형(ex: 고속도로 / its: 국도)]' +
  '&cctvType=[CCTV 유형(1: 실시간 스트리밍(HLS) / 2. 동영상 파일 / 3. 정지 영상]' +
  '&minX=[최소 경도 영역]' +
  '&maxX=[최대 경도 영역]' +
  '&minY=[최소 위도 영역]' +
  '&maxY=[최대 위도 영역]' +
  '&getType=[출력 결과 형식(xml, json / 기본: xml)]'
```

조회하고 싶은 cctv가 있는 위치의 영역을 먼저 알아야 한다.

이를 위해 벡터를 생성하기 위해 사용하던 `geojson.io`를 활용 하였다.

### 1. CCTV의 위치를 확인한다.

![image](https://github.com/user-attachments/assets/6885d1c8-739f-4fd1-a486-9c9d3833d425)

### 2. 대략적으로 CCTV가 위치하는곳에 대각선을 그린다.

![image](https://github.com/user-attachments/assets/9ea4c1dc-b721-4767-a3bb-56938fc28395)


### 3. 대각선이 그려진 영역의 좌표를 확인한다.

![image](https://github.com/user-attachments/assets/09ac7f33-e984-4efc-84eb-5b7623ded2f6)

### 4. 파라미터를 입력하고 요청을 보낸다.

```
  'https://openapi.its.go.kr:9443/cctvInfo' +
  '?apiKey=[발급받은 인증키]' +
  '&type=[도로 유형(ex: 고속도로 / its: 국도)]' +
  '&cctvType=[CCTV 유형(1: 실시간 스트리밍(HLS) / 2. 동영상 파일 / 3. 정지 영상]' +
  '&minX=126.73553402444435' +
  '&maxX=126.74002697586025' +
  '&minY=37.42163287416594' +
  '&maxY=37.42610492935842' +
  '&getType=[출력 결과 형식(xml, json / 기본: xml)]'
```

### 5. 응답을 확인한다. (일부 데이터는 제거함)

```
{
   "response":{
      "coordtype":1,
      "data":{
         "cctvurl2":"https://cctvsec.ktict.co.kr****",
         "roadsectionid":"",
         "coordx":126.737423,
         "coordy":37.423889,
         "cctvresolution":"",
         "filecreatetime":"",
         "cctvtype":3,
         "cctvformat":"JPEG",
         "cctvname":"[영동선]논현육교",
         "cctvurl":"http://imageurl****"
      },
      "datacount":1
   }
}
```
