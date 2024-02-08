# Closure 
def double_nos(lst1):
  def double(x):
    return x*2
  return lambda : [double(num) for num in lst1]
list1 = [1,2,3,4,5]
double_list = double_nos(list1)
print(double_list())
    
#Decorator
def doublex_nos(lst2):
  def doublex(x):
    return lst2[x]*2
  return lambda :{doublex(num) for num in lst2}
list2 =[1,2,3,4,5,6]


def doublex_list2():
  doublex_list2 = doublex_nos(list2)
  print(doublex_list2)

doublex_list2()
  
