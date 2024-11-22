import math
def find_solutions(a):
    sol1 = 0.5 * math.sqrt(2 - 2 * math.sqrt(1 - a**2 / (a**2 + 1)))
    sol2 = -sol1
    sol3 = 0.5 * math.sqrt(2 + 2 * math.sqrt(1 - a**2 / (a**2 + 1)))
    sol4 = -sol3
    if a <= 0:
        return [sol2, sol3] 
    else:
        return [sol4, sol1]
    
def main():
    T = int(input().strip())
    results = []
    for i in range(1, T + 1):
        a = float(input().strip())
        solutions = find_solutions(a)
        if solutions:
            results.append(f"Case #{i}: {' '.join(f'{sol:.4f}' for sol in solutions)}")
        else:
            results.append(f"Case #{i}: No Solution")
    print(*results, sep=" ")

if __name__ == "__main__":
    main()