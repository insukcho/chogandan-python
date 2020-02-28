import random                    # random 모듈 탑재

print('>> 숫자 맞추기 게임 <<')    # 게임 시작 알림

choice = random.randrange(100)   # 100 미만 임의 숫자 선택

while True:                      # 무한 루프 시작

    # 사용자에게 숫자 입력 요청 후 정수로 타입 변환
    user_choice = int(input('정수를 입력하세요: '))

    # 컴퓨터가 선택한 숫자와 입력받은 숫자가 맞으면 무한루프 탈출
    if choice == user_choice:
        break

    # 입력 숫자와 컴퓨터 선택 숫자 비교 및 정보 제공
    if choice < user_choice:
        print('너무 높아요!')
    else:
        print('너무 낮아요!')

# 무한 루프를 탈출했다는 의미는 숫자를 맞췄으니 프로그램 종료
print('정답입니다! 프로그램을 종료합니다.')
