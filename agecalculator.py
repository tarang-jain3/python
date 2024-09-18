bornyear=int(input("Enetr Yaer you born= "))
import datetime
x= datetime.datetime.now()
class AgeCalculator:
    age=x.year- bornyear
m=AgeCalculator()
print(m.age) 