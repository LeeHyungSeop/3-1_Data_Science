import os

def rename_files():
    directory = os.getcwd()  # 현재 작업 경로
    files = os.listdir(directory)  # 디렉터리 내의 파일 목록 가져오기
    
    for i, file in enumerate(files, start=1):
        if file.startswith("??"):
            if file.endswith(".ipynb"):  # .ipynb 확장자인 파일에 대해서만 작업 수행
                new_name = f"{i:02d}_{file}"  # 변경될 이름 생성
                os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
                print(f"Renamed file: {file} -> {new_name}")

        if len(file) >= 3 and file[2] == '-':
            new_name = file[:2] + '_' + file[3:]  # 파일명 변경
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            print(f"Renamed file: {file} -> {new_name}")

rename_files()
