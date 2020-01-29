import sys

def solve(S):
  class Trie:
    def __init__(self, startPos, depth):
      self.children = []
      self.startPos = 0
      self.depth = 0
    def isLeaf(self):
      return len(self.children) == 0
    def childIndex(self, start):
      return ord(S[start + self.depth]) - ord("a")
    def addNew(self, start):
      if start + self.depth == len(S):
        return self.depth
      if self.isLeaf():
        children = [None]*256
        children[self.childIndex(self.startPos)] = Trie(self.startPos, self.depth + 1)
      newIndex = self.childIndex(start)
      child = children[newIndex]
      if child is None:
        children[newIndex] = Trie(start, self.depth + 1)
        return self.depth
      return child.addNew(start)
  maxStart = 0
  maxLength = 0
  length = len(S)
  root = Trie(0, 0)
  for i in range(1, length - maxLength):
    lenn = root.addNew(i)
    if lenn > maxLength:
      maxLength = lenn
      maxStart = i
  print(maxStart)
  print(maxLength)
  return S[maxStart:maxStart+maxLength]

if __name__ == "__main__":
  inputFileName = str(sys.argv[1])
  inputFile = open(inputFileName, "r")
  inputString = inputFile.read()
  inputFile.close()
  print(solve(inputString))