import numpy as np
from itertools import permutations
from math import factorial, comb

def get_lower_pascal_matrix(n):
    """Generates an n x n lower triangular Pascal matrix L."""
    L = np.zeros((n, n), dtype=object)  # Use object for arbitrary-precision integers
    for i in range(n):
        for j in range(i + 1):
            L[i, j] = comb(i, j)
    return L

def calculate_apd(matrix, m):
    """Calculates the m-th order Alternating Power Difference (APD)."""
    n = matrix.shape[0]
    apd = 0
    # Generate all permutations in Sn
    for sigma in permutations(range(n)):
        # Calculate the sum of components based on the permutation
        f_sigma = sum(matrix[i, sigma[i]] for i in range(n))
        
        # Calculate the sign of the permutation (sgn(sigma))
        # Equivalent to (-1)^(number of inversions)
        inv_count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if sigma[i] > sigma[j]:
                    inv_count += 1
        sgn = (-1)**inv_count
        
        # Accumulate the Alternating Power Difference
        apd += sgn * (f_sigma ** m)
    return apd

def main():
    print(f"{'n':>2} | {'m1':>2} | {'APD_m1 (Computed)':>18} | {'(n-1)! (Theory)':>15} | {'Match'}")
    print("-" * 65)
    
    # Range n=2 to n=8 as discussed in the paper
    for n in range(2, 9):
        L = get_lower_pascal_matrix(n)
        m1 = n - 1
        computed_apd = calculate_apd(L, m1)
        expected_apd = factorial(n - 1)
        
        match = "YES" if computed_apd == expected_apd else "NO"
        print(f"{n:>2} | {m1:>2} | {computed_apd:>18} | {expected_apd:>15} | {match}")

if __name__ == "__main__":
    main()