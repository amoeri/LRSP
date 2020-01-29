#

# Instructions
## Generator
Run `generator.py` with parameters `[desired substring] [magnitude] [output file name]`
Desired Substring: Any string that should occur twice in the string
For example `py generator.py ThisIsSoAwesome9000 8 data.txt`
## Benchmark
Run `generator.py` with parameters `[desired substring] [logfile name] [time-out for each solution in seconds] [magnitude1] [magnitude2] [magnitude3] ...`
`py benchmark.py ThisIsSoAwesome9000 log.txt 1 6 7 8 9 10 11 12 13 14 15 16`
## Solutions
Each of the 3 solution can be run separately by running it with the input file name as a parameter.
For example `py naive.py data.txt`, `py dp.py data.txt` and `py suffixtree.py data.txt`
The scripts will output the result in the console.
Those will not time out.