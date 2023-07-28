# 패키지 설치
# 상단 햄버거 버튼 -> file -> settings -> project :Udemy
# -> python interpreter -> install(+ 버튼) 클릭 -> 패키지 검색/설치

from prettytable import PrettyTable

table = PrettyTable()
# PrettyTable 클래스의 table 객체 생성

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmandr"])
table.add_column("Type",["Electric", "Water", "Fire"])
# table 객체의 add_column 메서드 호출 -> 두 열을 추가
# 메서드 : 객체와 관련된 함수


print(table)
# 아래와 같이 생성
'''
+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmandr   |   Fire   |
+--------------+----------+
'''

print(table.align)
# {'base_align_value': 'c', 'Pokemon Name': 'c', 'Type': 'c'}
# table 객체의 align 속성 : c (가운데 정렬)임을 확인

table.align = 'l'
# table 객체 align 속성 변경 (왼쪽 정렬)

print(table)
'''
+--------------+----------+
| Pokemon Name | Type     |
+--------------+----------+
| Pikachu      | Electric |
| Squirtle     | Water    |
| Charmandr    | Fire     |
+--------------+----------+
'''
