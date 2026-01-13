import numpy as np
from itertools import permutations
from math import factorial, comb

def stirling2(n, k):
    """Calculates Stirling numbers of the second kind S2(n, k)."""
    if k == 0: return 1 if n == 0 else 0
    if k == n: return 1
    if k > n or k < 0: return 0
    res = 0
    for j in range(k + 1):
        term = ((-1)**(k - j)) * comb(k, j) * (j**n)
        res += term
    return res // factorial(k)

def get_lower_pascal_matrix(n):
    """Generates an n x n lower triangular Pascal matrix L."""
    L = np.zeros((n, n), dtype=object)
    for i in range(n):
        for j in range(i + 1):
            L[i, j] = comb(i, j)
    return L

def calculate_apd(matrix, m):
    """Calculates the m-th order Alternating Power Difference (APD)."""
    n = matrix.shape[0]
    apd = 0
    for sigma in permutations(range(n)):
        f_sigma = sum(matrix[i, sigma[i]] for i in range(n))
        inv_count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if sigma[i] > sigma[j]:
                    inv_count += 1
        sgn = (-1)**inv_count
        apd += sgn * (f_sigma ** m)
    return apd

def main():
    max_k = 6
    n_range = range(2, 7)
    
    print("% --- LaTeX Table Code Start ---")
    print("\\begin{table}[H]")
    print("\\centering")
    print(f"\\caption{{下三角パスカル行列 $L_n$ における $APD_{{m_k}}$ の計算結果 ($k=1 \\dots {max_k}$)}}")
    print("\\label{tab:apd_extended_k6}")
    print("\\small")
    # c: n, r: k=1..6
    print("\\begin{tabular}{crrrrrr}")
    print("\\toprule")
    print(" $n$ & $APD_{m_1}$ & $APD_{m_2}$ & $APD_{m_3}$ & $APD_{m_4}$ & $APD_{m_5}$ & $APD_{m_6}$ \\\\")
    print("\\midrule")
    
    for n in n_range:
        row_values = []
        for k in range(1, max_k + 1):
            m_k = n + k - 2
            val = calculate_apd(get_lower_pascal_matrix(n), m_k)
            # Add comma separators for large numbers
            row_values.append(f"{val:,}")
        
        print(f" {n} & {' & '.join(row_values)} \\\\")
    
    print("\\bottomrule")
    print("\\end{tabular}")
    print("\\end{table}")
    print("% --- LaTeX Table Code End ---")

if __name__ == "__main__":
    main()