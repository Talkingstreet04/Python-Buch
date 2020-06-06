import sys

try:
    argument1 = sys.argv[1]
except:
    argument1 = ""
try:
    argument2 = sys.argv[2]
except:
    argument2 = ""

if argument1 == "-a":
    print("lel")
