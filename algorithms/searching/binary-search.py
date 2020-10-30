import math

def binary_search(list: list, item_to_find):
  left = 0
  right = len(list) - 1
  while left <= right:
    mid = get_mid(left, right)
    if list[mid] > item_to_find:
      right = mid - 1
    elif list[mid] < item_to_find:
      left = mid + 1
    else:
      return mid
  return -1

def get_mid(left: int, right: int):
  # important parantheses
  return math.floor((left + right) / 2)

if __name__ == "__main__":
  # find an item that exists in the array
  find = 62
  list = [13,124,352,find,15,73,25,27]
  list = sorted(list)
  print(list)
  print(binary_search(list, find))

  # find an item that exists in the array and its the last item of the array
  find = 352
  list = [13,124,352,15,73,25,27]
  list = sorted(list)
  print(list)
  print(binary_search(list, find))

  # find an item that exists in the array and its the first item of the array
  find = 13
  list = [13,124,352,15,73,25,27]
  list = sorted(list)
  print(list)
  print(binary_search(list, find))

  # find an item that doesn't exists in the array
  find = 12
  list = [13,124,352,15,73,25,27]
  list = sorted(list)
  print(list)
  print(binary_search(list, find))