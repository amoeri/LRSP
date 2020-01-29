# LRSP
## Introduction
The [longest repeated substring problem](https://en.wikipedia.org/wiki/Longest_repeated_substring_problem), sometimes also called longest common duplicate, also with the addition of non-overlapping, is the problem of finding the longest substring of a string that occurs at least twice.
For the purpose of using it as an exercise to be handed out, you'll find in this repository:
1. A Python script to generate a random string of arbitrary length containing a specific desired substring twice and guaranteeing it is the longest, such that the solution can be easely checked.
2. A few example solutions written in Python, using different approaches, resulting in different space and time complexities
3. A benchmarking script that will run the example solutions on strings of different sizes to approximately measure the runtime to be expected for each

## Example Solutions
### Naive
| Time Complexity | Space Complexity | Difficulty |
| --------------- | ---------------- | -----------|
| O(n^3)          | O(n)             | very easy  |

### Dynamic Programming (DP)
### Suffix Array
### Suffix Tree

## Instructions
### Generator
Run `generator.py` with parameters `[desired substring] [magnitude] [output file name]`
Desired Substring: Any string that should occur twice in the string
For example `py generator.py ThisIsSoAwesome9000 8 data.txt`
### Benchmark
Run `generator.py` with parameters `[desired substring] [logfile name] [time-out for each solution in seconds] [magnitude1] [magnitude2] [magnitude3] ...`
`py benchmark.py ThisIsSoAwesome9000 log.txt 1 6 7 8 9 10 11 12 13 14 15 16`
### Solutions
Each of the 3 solution can be run separately by running it with the input file name as a parameter.
For example `py naive.py data.txt`, `py dp.py data.txt` and `py suffixtree.py data.txt`
The scripts will output the result in the console.
Those will not time out.