
def array_tut():
  
  # array data structure:
  numbers = [1, 2, 3, 4]

  #print(numbers)

  # loop over an array:
  """
  for num in numbers: 
    print(num)
  """

  # loop with index variable
  for i in range(len(numbers)):
    print(F"--{i}", numbers[i])

def lessonOne():
  print('---------------')  
  array_tut()
  print('---------------')  

lessonOne()