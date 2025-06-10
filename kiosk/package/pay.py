from . import valid

# 결제 여부 확인
def pay_deci():
    return input("주문이 확정되었습니다. 결제를 하시겠습니까? (y/n): ").lower().strip()

# 결제 화면 및 포인트 처리
def pay_screen(total_price, num_order, membership_dict):
    phone = None
    used_point = 0

    while True:
        use_point = input("포인트를 사용하시겠습니까? (y/n): ").lower().strip()
        if use_point == 'y':
            total_price, used_point, phone, membership_dict = use_membership_point(total_price, membership_dict)
            break
        elif use_point == 'n':
            break
        else:
            print("y 또는 n을 입력해주세요.")
    
    print(f"{total_price:,}원 결제하겠습니다. 카드를 삽입해주세요.")
    print("결제가 완료되었습니다.")
    
    if used_point == 0:
        while True:
            mem = input("포인트 적립 하시겠습니까? (y/n): ").lower().strip()
            if mem == 'y':
                membership_point_save(total_price, phone, membership_dict)
                break
            elif mem == 'n':
                break
            else:
                print("y 또는 n을 입력해주세요.")
    else:
        print("포인트를 사용하셨기 때문에 이번 결제는 적립되지 않습니다.")
        
    print(f"주문번호는 {num_order}번 입니다.")
    return membership_dict


# 포인트를 적립할 때 사용하는 함수
def membership_point_save(total_price, phone=None, membership_dict = {}):
    while not phone or not valid.is_valid_phone(phone):
        phone = input("전화번호를 입력해주세요 (- 없이): ").replace(" ", "")
        if not valid.is_valid_phone(phone):
            print("올바른 형식의 전화번호(예: 01012345678)를 입력해주세요.")
    points = int(total_price * 0.1)

    if phone in membership_dict:
        membership_dict[phone] += points
        print(f"{phone} 번호에 {points}포인트가 추가되어, 총 {membership_dict[phone]}포인트가 있습니다.")
    else:
        membership_dict[phone] = points
        print(f"{phone} 번호로 {points}포인트가 새로 적립되었습니다.")

# 포인트 사용 시 사용하는 함수
def use_membership_point(total_price, membership_dict):
    while True:
        phone = input("전화번호를 입력해주세요 (- 없이): ").replace(" ", "")
        if not valid.is_valid_phone(phone):
            print("올바른 형식의 전화번호(예: 01012345678)를 입력해주세요.")
            continue
        break
    if phone not in membership_dict:
        print("해당 번호로 적립된 포인트가 없습니다.")
        return total_price, 0, phone, membership_dict  # 사용된 포인트 없음

    available = membership_dict[phone]
    print(f"현재 {available}포인트가 있습니다.")
    while True:
        try:
            used_point = int(input("사용할 포인트를 입력해주세요: "))
            if used_point > available:
                print("포인트가 부족합니다.")
            elif used_point > total_price:
                print("결제 금액보다 많은 포인트는 사용할 수 없습니다.")
            elif used_point < 0:
                print("음수 포인트를 사용할 수 없습니다.")
            else:
                membership_dict[phone] -= used_point
                total_price -= used_point
                print(f"{used_point}포인트를 사용하여 {total_price}원을 결제합니다.")
                if membership_dict[phone] == 0:
                    del membership_dict[phone]
                return total_price, used_point, phone, membership_dict
        except ValueError:
            print("숫자를 입력해주세요.")