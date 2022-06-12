# class = 함수와 변수의 합 (빵 틀)
# object == instance = 클래스를 이용해서 만들어낸 것 (빵)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("안녕! " +  " 나는 " + self.name)


class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다, " +to_arrest)

class programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 이걸 만들자" + to_program)

wonie = Person("원이",20)
jenny = Police("제니", 21)
michael = programmer("마이클", 20)

wonie.say_hello()
jenny.say_hello()
jenny.arrest("너")
michael.program("너")