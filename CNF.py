class CNFClause:
    def __init__(self, literals):
        self.literals = set(literals)

    def satisfy(self, model):
        if(all(-lit in model for lit in self.literals)):
            return False
        return True

    def __repr__(self):
        return f"Clause({sorted(self.literals)})"

class CNFSentence:
    def __init__(self):
        self.clauses = set()

    def add_clause(self, literals):
        self.clauses.add(frozenset(literals))

    def satisfy(self, model):
        return all(CNFClause(clause).satisfy(model) for clause in self.clauses)

    def to_pysat_format(self):
        return [list(clause) for clause in self.clauses]
    
    def print_cnf(self):
            """In tất cả các clause trong CNF"""
            if not self.clauses:
                print("CNF is empty")
            else:
                print("CNF clauses:")
                for i, clause in enumerate(self.clauses, 1):
                    print(f"Clause {i}: {sorted(clause)}") 

