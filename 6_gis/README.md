# GIS

혼잡도를 지도에 표현하기 위해서 GIS를 사용하였다.

## OpenLayers

> 오픈레이어스는 오픈 소스 웹 브라우저에서 지도데이터를 표시하기위한 자바스크립트 라이브러리이다. <br/>
> 구글맵 또는 Bing맵 과 같은 웹 기반의 지리 응용 프로그램에 API를 제공한다.

OpenLayers에서는 `타일 지도 (Raster Map)` 와 `벡터 지도 (Vector Map)` 지도를 지원하며 각 특징은 아래와 같다.

### 타일 지도 (Raster Map)

타일 지도는 픽셀 기반의 이미지를 사용하여 지도를 표시한다. 일반적으로 OpenStreetMap(OSM)과 같은 서비스에서 제공하는 방식으로, 지도를 작은 이미지 조각(타일)으로 나누어 브라우저에서 필요한 부분만 불러온다.

#### 특징
 * 해상도가 고정되어 있으며, 확대/축소 시 이미지가 흐릿해질 수 있습니다.
 * 일반적으로 다양한 지리 정보(도로, 건물, 자연 등)를 포함하는 고해상도 이미지로 제공됩니다.

### 벡터 지도 (Vector Map)

벡터 지도는 수학적 표현(점, 선, 다각형 등)으로 지도를 표시한다. SVG(Scalable Vector Graphics) 형식으로 저장되며, 확대/축소 시 품질 손실이 없다.

#### 특징
 * 확대해도 선명하게 유지되며, 스타일링(색상, 두께 등)을 쉽게 조정할 수 있다.
 * 데이터 용량이 상대적으로 작고, 필요한 정보만 로드할 수 있어 효율적이다.
 * GIS 데이터(예: GeoJSON, Shapefile 등)와 잘 통합되어 사용된다.

## 선정

### ~~로컬 환경에서 인터넷이 되지 않아도 사용할 수 있으며, 로드로 인한 끊김이 없는 벡터 지도 방식을 사용하였다.~~

<details>
<summary>벡터 지도 데이터 [접기/펼치기]</summary>

## 벡터 지도 데이터

> 데이터 다운로드 : http://www.gisdeveloper.co.kr/?p=2332

![image](https://github.com/user-attachments/assets/04577d2c-5db3-4cc3-9298-3128235e2d1a)

해당 사이트에서 `Shapefile` 형식으로 데이터를 제공하고 있다.

이때 `Shapefile`란 `.dbf`, `.shp`, `.shx` 등으로 구성된 데이터 포맷을 의미한다.

하지만 OpenLayers에선 `Shapefile` 형식을 지원하지 않고 `GeoJSON` 형식만을 지원한다.

그렇기 때문에 먼저 `Shapefile` 형식으로 된 데이터를 `GeoJSON` 형식으로 변환해 줘야 한다.

## 컨버트

QGIS로 진행
</details>

### 타일 지도 방식을 선택하여 작업을 진행.

## 혼잡 표시

아래 구간별로 제공하는 CCTV를 분석하여

![image](https://github.com/user-attachments/assets/f9ebf421-1491-4560-82a0-a838858ea698)

`OpenLayers`를 통해 생성한 지도 위에 벡터로 혼잡도를 표시해야 된다.

![image](https://github.com/user-attachments/assets/9703ac56-e132-4d1a-b408-df4fd68d0dc7)

이를 위해선 구간별로 좌표를 알아야 하는데 <br/>
벡터 데이터를 시각적으로 작성하고 JSON 형태로 다운로드 할 수 있는 온라인 툴인 `GeoJSON.io`를 사용하였다.

> url : https://geojson.io/

![image](https://github.com/user-attachments/assets/de6d2d9d-1976-4f9d-b013-d8bb94ffdfa1)

이런식으로 선을 그리며 JSON 형태로 데이터를 생성한다.

이후 JSON 데이터를 불러와 지도 위에 벡터 데이터를 생성한다.
```
        // GeoJSON 파일로부터 벡터 데이터를 불러오는 벡터 소스 생성
        const vectorSource = new ol.source.Vector({
            url: '/static/map.geojson',  // GeoJSON 파일 경로
            format: new ol.format.GeoJSON()  // GeoJSON 형식으로 읽기
        });

        // 벡터 레이어 생성 (벡터 소스 사용)
        const vectorLayer = new ol.layer.Vector({
            source: vectorSource,
            style: new ol.style.Style({  // 벡터 데이터 스타일 설정
                stroke: new ol.style.Stroke({
                    color: 'gray',  // 선 색상 (초록)
                    width: 8  // 선 두께
                })
            })
        });

        // 지도 객체 생성
        const map = new ol.Map({
            target: 'map',  // 지도가 그려질 div ID
            layers: [
                rasterLayer,  // OSM 타일 레이어 추가
                vectorLayer  // GeoJSON 벡터 레이어 추가
            ],
            view: new ol.View({
                center: ol.proj.fromLonLat([127.024612, 37.532600]),  // 지도 중심 좌표 (경도, 위도: 서울)
                zoom: 12  // 줌 레벨 설정
            })
        });
```
