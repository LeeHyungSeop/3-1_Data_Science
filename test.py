import serial

# 시리얼 포트 연결
ser = serial.Serial('/dev/cu.usbmodem11101', 115200)

# 파일 열기
file = open('serial_data.txt', 'w')

while True:
    # 시리얼 포트에서 데이터 읽기
    data = ser.readline().decode('utf-8').strip()

    # 데이터 파일에 쓰기
    file.write(data + '\n')

    # 콘솔에 출력
    print(data)

    # 종료 조건
    if data == 'exit':
        break

# 파일과 시리얼 포트 닫기
file.close()
ser.close()
