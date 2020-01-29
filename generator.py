import sys
import random
import string

def generate(desiredSubstring, stringMagnitude):
  stringLength = pow(2, stringMagnitude)
  # define valid characterset
  characters = string.ascii_letters.join(string.digits)
  # generate string of desired length
  outputString = "".join(random.choice(characters) for i in range(stringLength - 2 * len(desiredSubstring)))
  # generate a substitute string for our desired substring and replace any occurences of the desiredSubstring
  substitute = desiredSubstring
  while(substitute == desiredSubstring):
    substitute = "".join(random.choice(characters) for i in range(len(desiredSubstring)))
  outputString = outputString.replace(desiredSubstring, substitute)
  # insert two occurences of the desiredSubstring at random locations
  position1 = random.randrange(0, stringLength)
  position2 = random.randrange(0, stringLength)
  while(abs(position1 - position2) < len(desiredSubstring)):
    position2 = random.randrange(0, stringLength)
  outputString = outputString[:position1] + desiredSubstring + outputString[position1:]
  outputString = outputString[:position2] + desiredSubstring + outputString[position2:]
  # TODO: check that there are no substrings of the same or longer length, if so replace them, special case when they contain the desired substring or the substitute
  return outputString

if __name__ == "__main__":
  desiredSubstring = str(sys.argv[1])
  stringMagnitude  = int(sys.argv[2])
  outputFileName = str(sys.argv[3])
  if pow(2, stringMagnitude) < len(desiredSubstring):
    print("String length must be larger than twice the length of the desired substring")
  else:
    outputString = generate(desiredSubstring, stringMagnitude)
    outputFile = open(outputFileName, "w")
    outputFile.write(outputString)
    outputFile.close()
    print(
      "A random string of length " 
      + str(len(outputString)) 
      + " containing substring \"" 
      + desiredSubstring 
      + "\" exactly twice and no other substring of equal length or longer appearing more than once has been written to " 
      + outputFileName)
  