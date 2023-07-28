##### step 0 #####
#### 클래스 만들기 ####

class User:
    pass # 클래스 선언 후 비워놓을 경우 pass 입력
# 객체생성
user_1 = User()
user_2 = User()



##### step 1 #####
##### 객체에 속성 부여하기 #####
user_1.id = "001"
user_1.username = "xxx"

user_2.id = "002"
user_2.username = "yyy"

print("step 1")
print(user_1.username)
# username 속성 : "xxx" 출력
# 위 경우 객체를 생성하고 속성을 부여하기 번거로움 -> 생성자로 속성을 쉽게 부여



##### step 2 #####
##### 생성자 생성하기 __init__ #####
class User2:
    def __init__(self, user_id, username): # 생성자 만들기 __init__
        # self : 클래스로 부터 만들어진 객체 자신을 지칭함.
        self.id = user_id # 객체 생성 시 user_id 입력시 id 속성은 user_id가 된다.
        self.username = username
        self.followers = 0 # 객체 생성 시 속성의 기본 값을 지정하고 싶을 때
        self.following = 0

# 생성자에 매개변수(user_id, username) 추가시 객체 생성 할 때마다 무조건 속성을 입력 해야 함.

user_1 = User2("001","xxx")
# id 속성 : 001 / username 속성 : xxx
user_2 = User2("002","yyy")
# id 속성 : 002 / username 속성 : yyy

print("\nstep 2")
print(user_1.id)
print(user_1.username)
print(user_1.followers)

print(user_2.id)
print(user_2.username)
print(user_2.followers)



##### step 3 #####
##### 클래스에 메서드 만들기 #####

class User3:
    # 생성자로 개체에 속성 지정
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    # 메서드 생성 -> 메서드의 경우 첫 매개변수로 self 자동 생성
    def follow(self, user):
        # 특정 user를 follow 하는 경우
        user.followers += 1 # user의 follower 수 +1
        self.following += 1 # 나(self)의 following 수 +1


user_1 = User3("001","xxx")
user_2 = User3("002","yyy")

user_1.follow(user_2)

print("\nstep 3")
print(user_1.following) # 1
print(user_1.followers) # 0
print(user_2.following) # 0
print(user_2.followers) # 1
