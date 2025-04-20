import markovify
import sys

# read text from a file
if len(sys.argv) != 2:
    sys.exit("behen ke lode, aise run kar: python markov.py text_file.txt")
with open(sys.argv[1]) as f:
    text = f.read()

# Train model
text_model = markovify.Text(text)

print()
for i in range(5):
    print(text_model.make_sentence())
    print()