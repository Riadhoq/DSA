"""
Binary Search Recursive
"""
# This was the first try
# this does not remember the actual index
# 
# def binary_search_first(list, item_to_find):
#   if len(list) == 0:
#     return -1
#   mid = len(list) // 2
#   # print(list)
#   if list[mid] == item_to_find:
#     # print(mid)
#     return mid
#   elif list[mid] > item_to_find:
#     binary_search(list[:mid], item_to_find)
#   else:
#     binary_search(list[mid:], item_to_find)

def binary_search(list, item_to_find):
  return binary_search_recursive(list, 0, len(list) - 1, item_to_find)

def binary_search_recursive(list, left, right, item_to_find):
  if left > right:
    return -1
  mid = (left + right) // 2
  # print(mid)
  if list[mid] == item_to_find:
    return mid
  elif list[mid] > item_to_find:
    # forgot to put return
    return binary_search_recursive(list, left, mid - 1, item_to_find)
  else:
    # forgot to put return
    return binary_search_recursive(list, mid + 1, right, item_to_find)  

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