
def array_tut():
  result = None

  # array data structure:
  numbers = [1, 2, 3, 4]

  #print(numbers)

  # loop over an array:
  """
  for num in numbers: 
    print(num)
  """

  # loop with index variable
  #for i in range(len(numbers)):
    #print(F"--{i}", numbers[i])

  # 1d array challenges:
  """
  1- Sum of Elements: 
  
  Calculate the sum of all elements in an array.
  """
  
  scores = [1, 2, 3, 4, 5]

  def sum_elements(elements):
    sum: int = 0

    for el in elements:
      sum += el
    
    return sum

  #result = sum_elements(scores) # 15

  """
  Maximum Element: Find the maximum element in an array.

  # bubble_sort

  # on each loop subtract 1 from the end of array

  [34, 1, 4, 2, 20, 6]
  [1, 4, 2, 20, 6, 34] =: no loop over 34
  [1, 2, 4, 6, 20, 34] =: no loop over 20
  [1, 2, 4, 6, 20, 34] => no swap happend so: break
  """

  def bubble_sort(elements):
    # bubble_sort

    n = len(elements)

    # we compare arr[0] to arr[0 + 1] =: so: n - 1 to not go out of bound
    for i in range(n - 1):
      #print('i:', i)
      # if: swapped not occurred =: break
      swapped = False
      holder = None

      # arr[inx + 1] so - 1
      # also: - i =: goes: - 0, - 1, - 2 =: in each loop 1 more element is in 
      # right place, cause big guys bubble to the end!!
      for j in range(0, n - i - 1):
        #print('j:', j)

        # if: greater than next =: swap
        if elements[j] > elements[j + 1]:
          holder = elements[j]
          elements[j] = elements[j + 1]
          elements[j + 1] = holder
          # swap happened
          swapped = True
      # if: no swapped =: break
      if not swapped:
        break
  
    # return 
    return elements

  unsorted = [34, 1, 4, 2, 20, 6]

  def find_max(elements):
    # just sort the array in assending order
    sorted = bubble_sort(elements)
    return sorted[-1]
    
  #result = find_max(unsorted)

  #============================================

  """
  Array Reversal: 
  
  Reverse the elements of an array in-place.

  """

  def reverseArr(arr):

    reversed = []
    # range(start, stop, step)
    # start: len(reversed) - 1 =: last index =: zero_based
    # stop: before -1 =: which is 0
    # step: -1 =: subtracts: 4, 3, 2, 1, 0
    print('--')
    for i in range(len(arr) - 1, -1, -1):
      # print(i) 4 to 0
      reversed.append(arr[i])
    return reversed

  # result = reverseArr([1, 2, 3, 4, 5]) # [5, 4, 3, 2, 1]

  #=======================================

  """
  Array Rotation: 
  
  Rotate the elements of an array left or right by a specified number of positions.


  # rotate to the left by 2: 
    # means: grab 2 items from the front and put at the end 
  
  # rotate to the right by 2:
    # means: grab 2 items from the end and put at the front

  # positive position: rotate to left
  # negative position: rotate to right
  """

  def rotateArr(arr: list, size: int, pos: int):

    # if: position out of range of array
    if abs(pos) > len(arr):
      return None

    # left: positive
    if (pos > 0):
      rotated_arr = []
      for i in range(pos, len(arr)):
        rotated_arr.append(arr[i])

      # from front to back
      for i in range(0, pos):
        rotated_arr.append(arr[i])

      return rotated_arr
    
    # right: negative
    if (pos < 0):
      rotated_arr = []
      for i in range(len(arr) - 1, len(arr) - 1 + pos, -1):
        print(i)
        rotated_arr.append(arr[i])

      for i in range(0, len(arr) + pos):
        rotated_arr.append(arr[i])

      return rotated_arr

    return []

  scores2 = [1, 2, 3, 4, 5]
  
  result = rotateArr(scores2, len(scores2), -2) # [1, 2]

  print('result: ', result)

def lessonOne():
  print('---------------')  
  array_tut()
  print('---------------')  

lessonOne()