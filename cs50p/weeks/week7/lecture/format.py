import re
import sys

name = input("What is your name").strip()

if matches := re.match(r"^(.+), *(.+)$", name):
    name = matches.group(1) + " " + matches.group(2)

print(f"Hello! {name}")