class student(object):
    def __init__(self, name, score):
        self.__name=name
        self.__score=score
    '''
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
        print('%s,%s' % (self.name,self.score))
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=80 and  self.score<90:
            return 'B'
        elif self.score>=60 and self.score<80:
            return 'c'
        else:return 'D' '''
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def  set_name(self,name):
        self.__name=name


    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
if __name__=="__main__":
    bai=student('baixin',90)

    print(bai.get_name())
