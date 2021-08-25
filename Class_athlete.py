'''
<클래스의 구성 >

class class_name: 펑션의 모임이 클래스
    def __init__(self): 초기화 펑션, 셀프라는 파라메터는 클래스 내부에서만 사용가능
                                   최소한의 펑션은 공유하자 라고하는게 셀프
    def function_name01(self): 펑션이름은 독특해야해
        return
    def function_name(self): 펑션은 독립적이다
        return
'''

class Athlete:
    def __init__(self,value='Jane'):
        self.inner_value = value #외부에서 들어온 것을 내부에 할당 시킴
        print(self.inner_value)

    def getInnerValue(self):
        return self.inner_value

# Athlete를 상속 받기
class Temp(Athlete):
    def __init__(self):
        super()#내부적으로 사용합니다

# 만들어진 클래스를 호출하고 어떻게 사용할지 아래에 기술
'''
 값을 아무것도 안 넣었을 때 초기화 시킨다고 인식해 __init__으로 호출 됨
 athlete = Athlete() 
 athlete = Athlete.__init__()
'''

athlete = Athlete(value='Juhee')

print(athlete.getInnerValue())