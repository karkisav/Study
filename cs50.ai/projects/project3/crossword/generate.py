import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable in self.domains.keys():
            valid_words = set()
            for word in self.domains[variable]:
                if len(word) == variable.length:
                    valid_words.add(word)
            self.domains[variable] = valid_words

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False
        overlap = self.crossword.overlaps[x,y]

        if overlap:
            x_index, y_index = overlap
            invalid_values = set()

            for value_x in self.domains[x]:
                has_corresponding_value = False

                for value_y in self.domains[y]:
                    if value_x[x_index] == value_y[y_index]:
                        has_corresponding_value = True
                        break
                    
                if has_corresponding_value == False:
                    invalid_values.add(value_x)
                    revised = True

            for value in invalid_values:
                self.domains[x].remove(value)

        return revised
    

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs is None:
            queue = []
            for variable in self.crossword.variables:
                for neighbour in self.crossword.neighbors(variable):
                    queue.append((variable, neighbour))
        else:
            queue = arcs

        while queue:
            X, Y = queue.pop()
            if self.revise(X, Y):
                if len(self.domains[X]) == 0:
                    return False
                for z in self.crossword.neighbors(X):
                    if z != Y:
                        queue.append((z,X))

        return True
    

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for variable in self.crossword.variables:
            if variable not in assignment.keys():
                return False
        return True
    

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        values = []
        for variable, value in assignment.items():
            if value in values:
                return False
            values.append(value)
            if len(value) != variable.length:
                return False
            for neighbour in self.crossword.neighbors(variable):
                if neighbour in assignment:
                    (i, j) = self.crossword.overlaps[variable, neighbour]
                    if value[i] != assignment[neighbour][j]:
                        return False
        return True
    

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        value_constraint = []
        for value in self.domains[var]:
            count = 0
            for neighbor in self.crossword.neighbors(var):
                if neighbor not in assignment:
                    (i, j) = self.crossword.overlaps[var, neighbor]
                    for neighbor_value in self.domains[neighbor]:
                        if neighbor_value in assignment and value[i] != assignment[neighbor_value][j]:
                            count += 1
            value_constraint.append((value, count))
        value_constraint.sort(key=lambda x: x[1])
        return [value for value, count in value_constraint]
                                                        

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned_variable = []
        for var in self.domains.keys():
            if var not in assignment:
                values = self.order_domain_values(var, assignment)
                degree = len(self.crossword.neighbors(var))
                unassigned_variable.append((var, len(values), degree))
        unassigned_variable.sort(key=lambda x: (x[1], -x[2]))
        return unassigned_variable[0][0]


    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if len(assignment) == len(self.crossword.variables):
            return assignment
        
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if value not in assignment:
                assignment[var] = value
                if self.consistent(assignment):
                    result = self.backtrack(assignment)
                    if result is not None:
                        return result
                    del assignment[var]
        return None
        


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
