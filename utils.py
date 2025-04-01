
def read_grid(filename):
    with open(f"testcases/{filename}", 'r') as f:
        lines = f.readlines()
    grid = [line.strip().split(', ') for line in lines]
    return grid

def write_grid(filename, algo, grid):
    with open(f"result/{algo}/{filename}", 'w') as f:
        for row in grid:
            f.write(', '.join(str(cell) for cell in row) + '\n')
        
def check_valid_grid(solution_grid):
    """
    Kiểm tra xem solution_grid có hợp lệ không dựa trên chính nó.
    - solution_grid: Lưới chứa số, 'T', hoặc 'G'.
    - Trả về True nếu hợp lệ, False nếu không.
    """
    rows = len(solution_grid)
    cols = len(solution_grid[0]) if rows > 0 else 0

    def get_neighbors(i, j):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return [(i + di, j + dj) for di, dj in directions if 0 <= i + di < rows and 0 <= j + dj < cols]

    for i in range(rows):
        for j in range(cols):
            cell = solution_grid[i][j]
            if cell.isdigit():  # Nếu ô chứa số
                expected_traps = int(cell)
                neighbors = get_neighbors(i, j)
                actual_traps = sum(1 for ni, nj in neighbors if solution_grid[ni][nj] == 'T')
                if actual_traps != expected_traps:
                    print(f"{float(i)}, {float(j)}, get flase")
                    return False  # Số trap không khớp với số trong ô
            elif cell not in ['T', 'G']:
                return False  # Ô không phải số phải là 'T' hoặc 'G'

    return True