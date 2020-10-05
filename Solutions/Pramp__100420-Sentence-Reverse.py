"""
Sentence Reverse

You are given an array of characters arr that consists of sequences of characters separated by space characters. 
Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
"""



"""
O(N), O(1) solution
step 1: loop thru the given arr : inverse the whole array;
step 2: reverse each word
"""
def _reverse(start, end, arr):
  i, j = start, end
  while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1

def reverse_words(arr):
  # step 1: reverse whe arr by whole 
  _reverse(0, len(arr) - 1, arr)
  
  # step 2: do swap for each word
  start = -1
  i = 0
  while i < len(arr):
    if arr[i] != " ":
      j = i
      while j + 1 < len(arr) and arr[j + 1] != " ":
        j += 1
      _reverse(i, j, arr)
      i = j
    i += 1
  return arr
