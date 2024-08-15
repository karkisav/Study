import sys

if len(sys.arg) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hellow my name is", arg)