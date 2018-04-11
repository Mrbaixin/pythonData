# class Student():
#     count=0
#     __slots__=('name','age')
#     def __init__(self, name):
#         self.name = name
#         Student.count=Student.count+1
#     def set_age(self, age):  # 定义一个函数作为实例方法
#         self.age = age
# # 开始创建实例
# stu1=Student('bai')
# stu2=Student('xin')
# print(Student.count)
# # 给实例动态添加属性
# stu1.age=20
# stu1.score=99
# print(stu1.age)
# stu1.set_age(22)
# print(stu1.age)
# 888888888888888888888888888888888888888 约束类
# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#
#     def get_score(self):
#          return self.__score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# if __name__=='__main__':
#     s=Student('bai',99)
#     s.set_score(60)
#     print(s.get_score())
# *************************************@property   方法变成属性
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth
s=Student()
s.score=60
print(s.score)
s.birth=1995
print(s.birth)
print(s.age)