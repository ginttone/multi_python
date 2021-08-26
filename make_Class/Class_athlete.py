'''
<클래스의 구성 >

class class_name: 펑션의 모임이 클래스
    def __init__(self): 초기화 펑션, 셀프라는 파라메터는 클래스 내부에서만 사용가능
                                   최소한의 펑션은 공유하자 라고하는게 셀프
                                   컴퓨터는 메모리만 쳐다본다. 클래스도 부르지않으면 동작 안한다. 불러서 메모리에 올리는것을 인스턴스라한다
                                   인스턴스 할 때 클래스를 초기화한다. 원래룰을 어기지 않고 지키면서 하는 방법은 클레스에 초기화시키는 펑션
                                    을 넣으면 호출되면서 자기자신을 호출시킨 것.
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

# Athlete를 Inheritance(상속) 받기
class InheritanceClass(Athlete):
    def __init__(self): #Inheritance 를 초기화 시킴
        # super()  #내부적으로 Athlete사용 합니다
        super().__init__() # Athlete 의 __init__()을 부르는 것

    def setValue(self,first_value):
        self.inherit_value = first_value # self변수 사용하려 지정

    def getValue(self):
        return self.inherit_value

# inherit = InheritanceClass() # 초기화
# Inheritance 값 호출하기 set->get
# print(inherit.getInnerValue())
# inherit.setValue(first_value='JuheeKim')
# print(inherit.getValue())

# Athlete에 있는 getInnerValue 를 사용해보기
# print(inherit.getInnerValue())

# 만들어진 클래스를 호출하고 어떻게 사용할지 아래에 기술
'''
 값을 아무것도 안 넣었을 때 초기화 시킨다고 인식해 __init__으로 호출 됨
   athlete = Athlete() 
== athlete = Athlete.__init__()
'''

# athlete = Athlete(value='Juhee')

# print(athlete.getInnerValue())

