import os
import xml.etree.ElementTree as ET

def convert_xml_to_yolo_format(xml_file, output_dir):
    # XML 파일 파싱
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 이미지 정보 가져오기
    images = root.findall('image')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 클래스 매핑
    class_mapping = {
        "truck": 0,
        "bus": 1,
        "car": 2
    }

    for image in images:
        image_name = image.attrib['name']
        image_width = int(image.attrib['width'])
        image_height = int(image.attrib['height'])
        
        txt_file_path = os.path.join(output_dir, f"{os.path.splitext(image_name)[0]}.txt")

        with open(txt_file_path, 'w') as txt_file:
            for box in image.findall('box'):
                label = box.attrib['label']
                if label not in class_mapping:
                    continue

                class_id = class_mapping[label]

                # YOLO 포맷에 맞게 bbox 좌표 계산
                xtl = float(box.attrib['xtl'])
                ytl = float(box.attrib['ytl'])
                xbr = float(box.attrib['xbr'])
                ybr = float(box.attrib['ybr'])

                # YOLO 포맷: <class_id> <x_center> <y_center> <width> <height>
                x_center = (xtl + xbr) / 2 / image_width
                y_center = (ytl + ybr) / 2 / image_height
                width = (xbr - xtl) / image_width
                height = (ybr - ytl) / image_height

                # 파일에 라인 추가
                txt_file.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

if __name__ == "__main__":
    xml_file_path = input("XML 파일 경로를 입력하세요: ")  # XML 파일 경로 수동 입력
    output_directory = input("저장할 디렉토리를 입력하세요: ")  # YOLO 형식의 TXT 파일이 저장될 디렉토리 수동 입력
    convert_xml_to_yolo_format(xml_file_path, output_directory)