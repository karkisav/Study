import termcolor

from logic import *

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, symbol):
            print(f"{symbol}: MAYBE")

knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)

check_knowledge(knowledge)

knowledge.add(And(
    Not(mustard), Not(kitchen), Not(revolver)
))

check_knowledge(knowledge)

knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

check_knowledge(knowledge)

knowledge.add(Not(plum))
knowledge.add(Not(ballroom))