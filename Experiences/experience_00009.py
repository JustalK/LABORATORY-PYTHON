class MyClass:
  variable = 20

  def __init__(self, a):
    self.variable = a

  def addVariable(self, a):
    print(self.variable + a) 

t = MyClass(10)

t.addVariable(10)
