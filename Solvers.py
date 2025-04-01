from pysat.solvers import Solver
from CNF import CNFSentence, CNFClause
from itertools import product

class GemHunterSolver:
    @staticmethod
    def solve_with_pysat(game):
        game.cnf = CNFSentence()
        cnf = game.generate_cnf()
        solver = Solver()
        for clause in cnf.to_pysat_format():
            solver.add_clause(clause)
        if solver.solve():
            model = {abs(lit): lit > 0 for lit in solver.get_model()}
            return game.interpret_solution(model)
        return None

    @staticmethod
    def solve_bruteforce(game):
        game.cnf = CNFSentence()
        game.generate_cnf()        
        game.cnf.print_cnf()


        empty_cells = [(i, j) for i in range(game.rows) for j in range(game.cols) if game.grid[i][j] == '_']
        
        for values in product([True, False], repeat=len(empty_cells)):
            assignment = {game.variable(empty_cells[i][0], empty_cells[i][1]): v for i, v in enumerate(values)}
            
            # Chuyển assignment thành model (set các literal)
            model = {var if val else -var for var, val in assignment.items()}
            
            # Truyền model vào satisfy(), không phải assignment
            if game.cnf.satisfy(model):
                return game.interpret_solution(assignment)
        
        return None  # Không tìm thấy giải pháp
    @staticmethod
    def solve_backtracking(game):
        game.cnf = CNFSentence()
        game.generate_cnf()
        empty_cells = [(i, j) for i in range(game.rows) for j in range(game.cols) if game.grid[i][j] == '_']
        
        def backtrack(assignment, index):
            if index == len(empty_cells):
                model = {var if val else -var for var, val in assignment.items()}
                if game.cnf.satisfy(model):
                    return assignment
                return None
            
            var = game.variable(empty_cells[index][0], empty_cells[index][1])
            
            # Thử gán True trước
            assignment[var] = True
            model = {v if assignment.get(v, False) else -v for v in assignment}
            if game.cnf.satisfy(model):
                result = backtrack(assignment, index + 1)
                if result is not None:
                    return result
            
            # Nếu True không được, thử False
            assignment[var] = False
            model = {v if assignment.get(v, False) else -v for v in assignment}
            if game.cnf.satisfy(model):
                result = backtrack(assignment, index + 1)
                if result is not None:
                    return result
            
            # Nếu cả hai đều không được, quay lui
            del assignment[var]
            return None
        
        assignment = {}
        solution = backtrack(assignment, 0)
        return game.interpret_solution(solution) if solution is not None else None
