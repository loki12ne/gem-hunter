from GemHunter import GemHunter
from Solvers import GemHunterSolver
import time
from utils import check_valid_grid


def brute_force(game, filename):
    time_start = time.time()
    solution = GemHunterSolver.solve_bruteforce(game)
    time_end = time.time()

    if solution:
        if check_valid_grid(solution):
            print("Good solution")
        else:
            print("Invalid solution")
        for row in solution:
            print(', '.join(row))
        from utils import write_grid
        write_grid(f"output_{filename.split('.')[0]}.txt","brute_force", solution)
    else:
        print("No solution found")
    print(f"Time: {(time_end - time_start) * 1000:0.9f}ms")
    
def backtracking(game, filename):
    time_start = time.time()
    solution = GemHunterSolver.solve_backtracking(game)
    
    time_end = time.time()

    if solution:
        if check_valid_grid(solution):
            print("Good solution")
        else:
            print("Invalid solution")
        for row in solution:
            print(', '.join(row))
        from utils import write_grid
        write_grid(f"output_{filename.split('.')[0]}.txt", "backtracking", solution)
    else:
        print("No solution found")
    print(f"Time: {(time_end - time_start) * 1000:0.9f}ms")



def pysat(game, filename):
    time_start = time.time()
    solution = GemHunterSolver.solve_with_pysat(game)
    time_end = time.time()

    if solution:
        if check_valid_grid(solution):
            print("Good solution")
        else:
            print("Invalid solution")
        for row in solution:
            print(', '.join(row))
        from utils import write_grid
        write_grid(f"output_{filename.split('.')[0]}.txt","pysat", solution)
    else:
        print("No solution found")
    print(f"Time: {(time_end - time_start) * 1000:0.9f}ms")
    
def compare_algorithms():
    values = [5, 9, 11, 15, 20]
    while True:
        print("Comparing algorithms:")
        print("Choose the algorithm:")
        print("1. Brute Force")
        print("2. Backtracking")
        print("3. PySAT")
        print("4. Exit")
        
        algorithm = int(input("Enter the number of the algorithm: "))
        if algorithm == 4:
            break
        for N in values:
            filename = f"input{N}x{N}.txt"
            game = GemHunter(filename)
            print(f"with {N} x {N} input: ")
            if algorithm == 1:
                brute_force(game, filename)
            elif algorithm == 2:
                backtracking(game, filename)
            elif algorithm == 3:
                pysat(game, filename)
            elif algorithm == 4:
                print(f"Running all algorithms for {filename}...")
                brute_force(game, filename)
                backtracking(game, filename)
                pysat(game, filename)
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
                break


def main():
    print("Choose the algorithm:")
    print("1. Brute force")
    print("2. Backtracking")
    print("3. PySAT")
    print("4. Compare 3 algorihms")
    algorithm = int(input("Enter the number of the algorithm: "))

    if algorithm == 4:
        compare_algorithms()
        return

    filename = input("File test case input: ")
    game = GemHunter(filename)

    print("Input:")
    for row in game.grid:
        print(', '.join(row))
    print()

    if algorithm == 1:
        brute_force(game, filename)
    elif algorithm == 2:
        backtracking(game, filename)
    elif algorithm == 3:
        pysat(game, filename)
    else:
        print("Invalid choice")
        return


if __name__ == "__main__":
    main()