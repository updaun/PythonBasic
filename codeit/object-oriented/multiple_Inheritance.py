# 엔지니어 클래스
class Engineer:
    def __init__(self, favorite_language):
        self.favorite_language = favorite_language

    def program(self):
        print("{}(으)로 프로그래밍합니다.".format(self.favorite_language))


# 테니스 선수 클래스
class TennisPlayer:
    def __init__(self, tennis_level):
        self.tennis_level = tennis_level

    def play_tennis(self):
        print("{} 반에서 테니스를 칩니다.".format(self.tennis_level))


# 엔지니어 이면서 테니스 선수이라면??
class EngineerTennisPlayer(Engineer, TennisPlayer):
    # 오버라이딩
    def __init__(self, favorite_language, tennis_level):
        # super 메소드를 사용하기 애매한 단점이 발생
        Engineer.__init__(self, favorite_language)    
        TennisPlayer.__init__(self, tennis_level)

# 테스트

# 다중 상속을 받는 클래스의 인스턴스 생성
younghoon = EngineerTennisPlayer("파이썬", "초급")

# 두 부모 클래스의 메소들들을 잘 물려받았는지 확인
younghoon.program()
younghoon.play_tennis()