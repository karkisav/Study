import sys

if len(sys.argv) < 2:
    sys.exit("Too Few Arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many Arguments")
else:
    print("Hello, my name is", sys.argv[1])