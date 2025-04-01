from CNF import CNFSentence, CNFClause
from itertools import combinations

class GemHunter:
    def __init__(self, filename):
        from utils import read_grid
        self.grid = read_grid(filename)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.cnf = None  
        self.known_cells = {(i, j): int(self.grid[i][j]) for i in range(self.rows) 
                            for j in range(self.cols) if self.grid[i][j].isdigit()}

    def get_unknown_neighbors(self, i, j):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return [(i + di, j + dj) for di, dj in directions 
                if 0 <= i + di < self.rows and 0 <= j + dj < self.cols 
                and self.grid[i + di][j + dj] == '_']

    def variable(self, i, j):
        return i * self.cols + j + 1

    def generate_cnf(self):
        if self.cnf is None:
            raise ValueError("self.cnf chưa được khởi tạo bởi Solver")
        
        for (i, j), k in self.known_cells.items():
            neighbors = self.get_unknown_neighbors(i, j)
            variables = [self.variable(x, y) for x, y in neighbors]
            self.add_exactly_k_traps(variables, k)
        return self.cnf
        
    def add_exactly_k_traps(self, variables, k):
        n = len(variables)
        if k < 0 or k > n:
            return
        
        if k == n :
            for var in variables:
                self.cnf.add_clause({var})  
            return
        
        for comb in combinations(variables, n - k + 1):
            self.cnf.add_clause(set(comb))  

        for comb in combinations(variables, k + 1):
            self.cnf.add_clause({-x for x in comb})

    def interpret_solution(self, model):
        result = [row[:] for row in self.grid]
        for i in range(self.rows):
            for j in range(self.cols):
                if result[i][j] == '_':
                    var = self.variable(i, j)
                    result[i][j] = 'T' if model.get(var, False) else 'G'
        return result
    