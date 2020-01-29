import sys

def solve(inputString):
  inputStringLength = len(inputString) 
  LCSRe = [[0 for x in range(inputStringLength + 1)]  
              for y in range(inputStringLength + 1)] 
  longestSubstring = "" 
  longestSubstringLength = 0
  index = 0
  for i in range(1,inputStringLength + 1): 
    for j in range(i + 1,inputStringLength + 1): 
      if (inputString[i - 1] == inputString[j - 1] and
        LCSRe[i - 1][j - 1] < (j - i)): 
        LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1
        if (LCSRe[i][j] > longestSubstringLength): 
          longestSubstringLength = LCSRe[i][j] 
          index = max(i, index)      
      else: 
        LCSRe[i][j] = 0
  if (longestSubstringLength > 0): 
    for i in range(index - longestSubstringLength + 1, index + 1): 
      longestSubstring = longestSubstring + inputString[i - 1] 
  return longestSubstring 

  if __name__ == "__main__":
    inputFileName = str(sys.argv[1])
    inputFile = open(inputFileName, "r")
    inputString = inputFile.read()
    inputFile.close()
    print(solve(inputString))