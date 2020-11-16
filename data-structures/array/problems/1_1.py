"""
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures.
"""

def isUniqueStr(inputString: str) -> bool :
  """Returns True if inputString is unique
    uses HashMap, time O(N), space 0(N)
    """
  seen = dict()
  for char in inputString:
    # print(char)
    if seen.get(char):
      return False
    else:
      seen[char] = True
  return True

def isUniqueStrAlt(inputString: str):
  """Returns True if inputString is unique
    using bit manipulation, time O(N), space 0(1)
    Only works for lowercase a-z
  """
  checker = 0
  for char in inputString:
    val = ord(char) - ord('a')
    if checker & (1 << val) > 0: # checking if a bit is stored at the position already
      return False
    checker = checker | (1 << val) # basically storing bits based on the how big the {val} is
    print(bin(checker))
  return True
if __name__ == "__main__":
    print(isUniqueStr("ddf"))
    print(isUniqueStrAlt("dafz"))
