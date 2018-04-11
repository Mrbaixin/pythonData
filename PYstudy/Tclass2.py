class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def resolution(self):
       return self._height*self._width

sc1=Screen()
sc1.width=10
sc1.height=20
print(sc1.resolution)
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
