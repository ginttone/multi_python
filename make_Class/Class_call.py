# Class_athlete.py 의 class 호출해서 쓰기
from make_Class.Class_athlete import Athlete

#Athlete 초기화
athlete = Athlete()
print(athlete.getInnerValue())

from make_Class import Class_athlete as ca

inherit = ca.InheritanceClass()
print(inherit.getInnerValue())