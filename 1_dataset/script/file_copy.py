import os
import shutil

def copy_files_only(source_dir, destination_dir):
    # 디렉터리가 존재하는지 확인하고, 없으면 생성
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"'{destination_dir}' 디렉터리가 생성되었습니다.")

    # os.walk를 사용하여 모든 하위 디렉터리 및 파일을 탐색
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            source_file_path = os.path.join(root, filename)
            
            # 파일만 복사
            destination_file_path = os.path.join(destination_dir, filename)
            shutil.copy(source_file_path, destination_file_path)
            print(f"'{source_file_path}' 파일이 '{destination_file_path}'로 복사되었습니다.")

# 사용자 입력으로 디렉터리 경로 설정
source_directory = input("복사할 파일들이 있는 디렉터리를 입력하세요: ")
destination_directory = input("파일을 복사할 디렉터리를 입력하세요: ")

# 파일 복사 수행
copy_files_only(source_directory, destination_directory)
