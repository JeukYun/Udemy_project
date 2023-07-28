# 각 클래스에 대한 정보 확인
# https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
# Menu 클래스로 menu 객체 생성
coffee_maker = CoffeeMaker()
# CoffeeMaker 클래스로 coffee_maker 객체 생성
money_machin = MoneyMachine()
# MoneyMachine 클래스로 money_machin 객체 생성

# money_machin.report()
# 현재 커피 머신 잔액
# coffee_maker.report()
# 남은 재료

coffee_make = True


while coffee_make:
    coffee = input(f"What would you like? ({menu.get_items()}):")

    if coffee == "report":
        coffee_maker.report()
        money_machin.report()

    elif coffee == "off":
        coffee_make = False

    else:
        menu_item = menu.find_drink(coffee)
        # menu 클래스에 find_drink() 메서드 호출 시 MenuItem 객체 반환
        # 반환된 객체를 menu_item 이름의 객체로 저장
        # print(menu_item) -> MenuItem 객체의 위치값 반환

        if coffee_maker.is_resource_sufficient(menu_item):
            # is_resource_sufficient() 함수의 입력값 : MenuItem 객체
            # 재료 확인 -> 충분치 않은 경우 False 반환
            print(f"Your {coffee} cost is ${menu_item.cost}")

            if money_machin.make_payment(menu_item.cost):
                # money_machin 객체의 make_payment() 함수 호출
                # make_payment() 함수 입력 값에 menu_item 의 cost 속성 호출
                coffee_maker.make_coffee(menu_item)
        else:
            coffee_make = False

