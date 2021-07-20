import unittest

def maxOnesAfterRemoveItem(input):
  state = "start"
  c, c2 = 0, 0
  maxLen = 0
  allOnes = True

  for i in range(len(input)):
    if state == "start" and input[i] == 0:
      allOnes = False
    elif state == "start" and input[i] == 1:
      c += 1
      state = "one"
    elif state == "one" and input[i] == 0:
      allOnes = False
      state = "zero"
    elif state == "one" and input[i] == 1:
      c += 1
    elif state == "zero" and input[i] == 0:
      allOnes = False
      maxLen = max(maxLen, c + c2)
      c, c2 = 0, 0
      state = "start"
    elif state == "zero" and input[i] == 1:
      c2 = c
      c = 1
      state = "one"
      maxLen = max(maxLen, c + c2)
  maxLen = max(maxLen, c + c2)
  if allOnes:
    maxLen -= 1
  return maxLen
      
# tests
class TestMaxOnes(unittest.TestCase):
  def test1(self):
    self.assertEqual(maxOnesAfterRemoveItem([0,0]), 0)
  def test2(self):
    self.assertEqual(maxOnesAfterRemoveItem([0,1]), 1)
  def test3(self):
    self.assertEqual(maxOnesAfterRemoveItem([1,0]), 1)
  def test4(self):
    self.assertEqual(maxOnesAfterRemoveItem([1,1]), 1)
  def test5(self):
    self.assertEqual(maxOnesAfterRemoveItem([1, 1, 0, 1, 1]), 4)
  def test6(self):
    self.assertEqual(maxOnesAfterRemoveItem([1, 1, 0, 1, 1, 0, 1, 1, 1]), 5)
  def test7(self):
    self.assertEqual(maxOnesAfterRemoveItem([1, 1, 0, 1, 1, 0, 1, 1, 1, 0]), 5)
  def test8(self):
    self.assertEqual(maxOnesAfterRemoveItem([1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1]), 5)
  def test9(self):
    self.assertEqual(maxOnesAfterRemoveItem([1, 1, 0, 1, 0, 1]), 3)

if __name__ == "__main__":
  unittest.main()
