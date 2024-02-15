''' Problem Statement: Your task is to write a function that solves the
Tower of Hanoi puzzle for 'n' disks. The function should print or return
the steps needed to move 'n' disks from the first peg to the third peg,
following the classic rules:

Only one disk can be moved at a time.

Each move consists of taking the upper disk from one of the stacks
and placing it on top of another stack.

No disk may be placed on top of a smaller disk.

Example: For n = 3, the minimum number of moves is 7.
The sequence of moves would be represented as a series of steps or instructions.

Guidelines:

Implement your solution in any programming language.

Focus on creating a clear and efficient algorithm.

Bonus Challenge: Can your function also count the total number of moves?'''

# use the 'divide and conquer' strategy
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return 1  # base case - only one disk to move
    
    # move a tower of size n-1 from source peg to auxiliary peg
    count1 = tower_of_hanoi(n - 1, source, target, auxiliary)
    
    # move largest disk from source peg to target peg
    print(f"Move disk {n} from {source} to {target}")
    
    # move tower of size n-1 from auxiliary peg to target peg
    count2 = tower_of_hanoi(n - 1, auxiliary, source, target)
    
    return count1 + 1 + count2  # total moves = moves for smaller tower + 1 move for largest disk + moves for smaller tower

# test function with given example of n = 3
n = 3
source = 'A'
auxiliary = 'B'
target = 'C'
total_moves = tower_of_hanoi(n, source, auxiliary, target)
print("Total number of moves:", total_moves)
