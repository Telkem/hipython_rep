# 유효한 숫자 입력을 받기 위한 함수
def get_valid_number_input(msg, min_no = 1, max_no = 5):
    try:
        number = int(input(msg))
        if number < min_no:
            print(f"{min_no} 이상 숫자를 입력하세요")
            return None
        elif number > max_no:
            print(f"{max_no} 이하 숫자를 입력하세요")
            return None
        else:
            return number
    except ValueError:
        print("숫자를 입력하세요")
        return None
# 유효한 전화번호인지 확인하기 위한 함수
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 11 and phone.startswith('010')