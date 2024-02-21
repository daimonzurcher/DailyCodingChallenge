''' Problem Statement: Design an algorithm that solves the classic logic puzzle: given a
set of clues, determine the correct sequence of elements (e.g., who lives in which house,
with what pet, and drinks what beverage). The challenge is to create a solution that is
both efficient and scalable, capable of handling an increasing number of elements and clues.

Example:

There are five houses in five different colors.

In each house lives a person with a different nationality.

These five owners drink a certain type of beverage, smoke a certain brand of cigar, and keep a certain pet.

No owners have the same pet, smoke the same brand of cigar, or drink the same beverage.

Guidelines:

You can use any programming language to implement your solution.

Focus on creating a readable and efficient algorithm that can deduce the solution from the given clues.

Bonus: Can your algorithm provide solutions for variations of the puzzle with more elements and clues? '''

# had to look up what 'constraint satisfaction' is to try and tackle this problem

import itertools

def solve_puzzle():
    # define possible values for each property
    colors = ["blue", "red", "green", "yellow", "orange"]
    nationalities = ["English", "Spanish", "Japanese", "African", "British"]
    beverages = ["coffee", "water", "juice", "milk", "soda"]
    cigars = ["Ashton", "Arturo Fuente", "Oliva", "La Aroma de Cuba", "Padron"]
    pets = ["cat", "dog", "turtle", "gecko", "hamster"]
    
    # generate all possible perms of property combos
    permutations = list(itertools.permutations(range(1, 6)))
    
    # initialize solution state before
    solution_found = False

    # iterate through each perm and check if it satisfies all clues
    for perm in permutations:
        # mappings for each property based on current perm
        mapping = {
            "colors": dict(zip(range(1, 6), perm)),
            "nationalities": dict(zip(range(1, 6), perm)),
            "beverages": dict(zip(range(1, 6), perm)),
            "cigars": dict(zip(range(1, 6), perm)),
            "pets": dict(zip(range(1, 6), perm))
        }
        
        # Clues from the puzzle
        # 1. The Englishman lives in the red house.
        if mapping["colors"][2] != mapping["nationalities"][1] == "English":
            continue
        
        # 2. The Spaniard owns the dog.
        if mapping["nationalities"][2] != mapping["pets"][2] == "Spanish":
            continue
        
        # 3. Coffee is drunk in the green house.
        if mapping["colors"][3] != mapping["beverages"][1] == "coffee":
            continue
        
        # 4. The Japanese drinks water.
        if mapping["nationalities"][3] != mapping["beverages"][2] == "Japanese":
            continue
        
        # 5. The green house is immediately to the right of the ivory house.
        if mapping["colors"][3] != mapping["colors"][2] + 1:
            continue
        
        # 6. The Ashton smoker owns cats.
        if mapping["cigars"][1] != mapping["pets"][1] == "Ashton":
            continue
        
        # 7. Arturo Fuente is smoked in the yellow house.
        if mapping["colors"][5] != mapping["cigars"][2] == "Arturo Fuente":
            continue
        
        # 8. Milk is drunk in the middle house.
        if mapping["beverages"][3] != 3:
            continue
        
        # 9. The African lives in the first house.
        if mapping["nationalities"][1] != 1 == "African":
            continue
        
        # 10. The man who smokes La Aroma de Cuba lives next to the man with the turtle.
        if abs(mapping["cigars"][4] - mapping["pets"][4]) != 1:
            continue
        
        # 11. The Padron smoker drinks soda.
        if mapping["beverages"][5] != mapping["cigars"][5] == "Padron":
            continue
        
        # 12. The British smokes Oliva.
        if mapping["nationalities"][5] != mapping["cigars"][3] == "British":
            continue
        
        # 13. The dog owner drinks juice.
        if mapping["pets"][5] != mapping["beverages"][3] == "dog":
            continue
        
        # 14. The gecko owner lives next to the orange house.
        if abs(mapping["pets"][4] - mapping["colors"][5]) != 1:
            continue
        
        # solution found --> print final mapping
        solution_found = True
        for prop in mapping:
            print(prop.capitalize() + ":")
            for pos, val in mapping[prop].items():
                print("House", pos, "-", val)
            print("\n")
        break

    # if no solution found, print that
    if not solution_found:
        print("No solution found.")

# solve the puzzle
solve_puzzle()