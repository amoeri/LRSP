import sys
from datetime import datetime
from time import time
from func_timeout import func_timeout, FunctionTimedOut

import generator
import naive
import dp
import suffixtree

ms = lambda: int(round(time() * 1000))

class Logger:
  def __init__(self, outputFileName):
    self.outputFileName = outputFileName
  def log(self, log):
    line = str(datetime.now()) + ' | ' + log
    outputFile = open(self.outputFileName, "a")
    outputFile.write(line + "\n")
    outputFile.close() 
    print(log)

if __name__ == "__main__":
  desiredSubstring = str(sys.argv[1])
  logFileName  = str(sys.argv[2])
  timeout = int(sys.argv[3])
  log = Logger(logFileName).log
  print("Log will also be written to " + logFileName)
  log("Running new benchmark with substring \"" + desiredSubstring + "\"")
  log("3 Solutions are beeing run: 1. Naive O(n^3) 2. DP O(n^2) 3. Suffix Tree O(n*log^2(n))")
  log("Magnitude | O(n^3) Time [ms] | O(n^2) Time [ms] | O(n)   Time [ms]")
  log("----------|------------------|------------------|-----------------")
  for i in range(4, len(sys.argv)):
    magnitude = int(sys.argv[i])
    if pow(2, magnitude) < len(desiredSubstring):
      line = str(magnitude).rjust(9) + " | Error: String length must be larger than twice the length of the desired substring"
    else:
      line = str(magnitude).rjust(9) + " | "
      inputString = generator.generate(desiredSubstring, magnitude)
      # Naive
      try:
        startTimeNaive = ms()
        resultNaive = func_timeout(timeout, naive.solve, args=(inputString,))
        endTimeNaive = ms()
        if resultNaive == desiredSubstring:
          line += str(endTimeNaive - startTimeNaive).rjust(13) + " ms | "
        else:
          line += "wrong answer     | "
      except FunctionTimedOut:
        line += "timeout (" + str(timeout) + "s)     | "        
      # DP
      try:
        startTimeDP = ms()
        resultDP = func_timeout(timeout, dp.solve, args=(inputString,))
        endTimeDP = ms()
        if resultDP == desiredSubstring:
          line += str(endTimeDP - startTimeDP).rjust(13) + " ms | "
        else:
          line += "wrong answer     | "
      except FunctionTimedOut:
        line += "timeout (" + str(timeout) + "s)     | "        
      # Suffix
      try:
        startTimeSuffix = ms()
        resultSuffix = func_timeout(timeout, suffixtree.solve, args=(inputString,))
        endTimeSuffix = ms()
        if resultSuffix == desiredSubstring:
          line += str(endTimeSuffix - startTimeSuffix).rjust(13) + " ms"
        else:
          line += "wrong answer    "
      except FunctionTimedOut:
        line += "timeout (" + str(timeout) + "s)     | "        
    log(line)
  log("----------|------------------|------------------|-----------------")
  log("End of benchmark")
    