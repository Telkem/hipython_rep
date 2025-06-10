from . import valid

# 장바구니 상태를 보여주는 함수
def display_cart(cart, total_price):
    print("\n" + "=" * 40)
    print("현재 장바구니")
    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
    print("-" * 40)
    print(f"Total = {total_price:,}원")

# 토핑을 장바구니에 추가하는 함수
def add_menu(cart, total_price, menu_list):
    current_total = sum(item['quantity'] for item in cart)
    remaining = 16 - current_total  # 최대 15개까지 가능

    if remaining <= 0:
        print("장바구니에는 최대 16개까지만 담을 수 있습니다.")
        return total_price

    print("\n메뉴 목록:")
    for i, item in enumerate(menu_list, start=1):
        print(f"{i}. {item['name']} : {item['price']:,}원")
    idx = valid.get_valid_number_input("추가할 토핑 번호를 골라주세요 : ", 1, len(menu_list))
    if idx:
        idx -= 1
        qty = valid.get_valid_number_input(f"수량을 선택해주세요 (남은 수량: {remaining}) : ",1,remaining)
        if qty:
            selected_item = menu_list[idx]
            # 기존에 있던 토핑이면 수량만 증가
            for item in cart:
                if item['name'] == selected_item['name']:
                    item['quantity'] += qty
                    break
            else:
                # 새로운 항목 추가
                cart.append({'name': selected_item['name'], 'quantity': qty, 'price': selected_item['price']})
            total_price += selected_item['price'] * qty
    return total_price


# 장바구니에서 메뉴를 삭제하는 함수
def del_menu(cart, total_price):
    if not cart:
        print("장바구니가 비어 있어 삭제할 수 없습니다.")
        return total_price
    display_cart(cart, total_price)
    idx = valid.get_valid_number_input("삭제할 메뉴의 번호를 골라주세요 : ",1,len(cart))
    if idx:
        idx -= 1
        item = cart[idx]
        print(f"'{item['name']}'의 현재 수량: {item['quantity']}")
        del_qty = valid.get_valid_number_input("몇 개를 삭제하시겠습니까? : ", 1, item['quantity'])
        if del_qty:
            item['quantity'] -= del_qty
            if item['quantity'] == 0:
                cart.pop(idx)
            total_price -= item['price'] * del_qty
            print(f"'{item['name']}' {del_qty}개가 삭제되었습니다.")
    return total_price