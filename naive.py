import sys

def solve(inputString):
  longestSubstring = ""
  for substringStartPosition in range(0, len(inputString) - 1):
    for substringLength in range(len(longestSubstring), len(inputString) - 1 - substringStartPosition):
      if inputString[substringStartPosition:substringStartPosition+substringLength] in inputString[substringStartPosition+substringLength+1:]:
        longestSubstring = inputString[substringStartPosition:substringStartPosition+substringLength]
  return longestSubstring

if __name__ == "__main__":
  inputFileName = str(sys.argv[1])
  inputFile = open(inputFileName, "r")
  inputString = inputFile.read()
  inputFile.close()
  print(solve(inputString))