# Pascal-APD Research Toolkit

This repository contains Python scripts for verifying and reproducing the mathematical discovery of **Self-Similar Alternating Power Difference (APD) Structures** in Pascal matrices.

## Overview

The Alternating Power Difference (APD) is a novel matrix invariant defined through the symmetric group $S_n$. This toolkit provides two primary scripts to validate the theoretical findings:

1. **Fundamental Verification (`verify_apd.py`)**: Validates the initial invariant $\operatorname{APD}_{n-1}(L_n) = (n-1)!$.
2. **Table Reproduction (`reproduce_table.py`)**: Generates an extended LaTeX table for higher-order APD values, demonstrating the connection to **Stirling numbers of the second kind**.

## Mathematical Definition

For an $n \times n$ matrix $A$, the $m$-th order APD is defined as:
$$\operatorname{APD}_m(A) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \left( \sum_{i=0}^{n-1} A_{i, \sigma(i)} \right)^m$$

### Key Discovery: The Stirling Connection
Our research identifies that for triangular Pascal matrices $L_n$ and $U_n$, the APD values follow a pure closed-form:
$$\operatorname{APD}_{n+k-2}(L_n) = (n-1)! \times \begin{Bmatrix} n+k-1 \\ n \end{Bmatrix}$$
where $\begin{Bmatrix} n \\ k \end{Bmatrix}$ denotes Stirling numbers of the second kind.

## Prerequisites

- Python 3.x
- NumPy

## Usage

### Program 1: Basic Verification
This script verifies the core theorem for $n=2$ to $n=8$.
```bash
python verify_apd.py

```

### Program 2: Extended Data Reproduction

This script generates the LaTeX source code for the extended APD table used in the paper.

```bash
python reproduce_table.py

```

## Computational Complexity

Since these verification scripts use an exhaustive permutation search to ensure mathematical fidelity to the definition, the complexity is .

* **Feasible range**:  on standard consumer CPUs.
* **For **: We recommend the "APD Generating Triangle" (Difference Engine) approach described in the paper.

## Research Context

This work explores the emergence of combinatorial structures from linear algebraic invariants, specifically focusing on the intersection of the symmetric group and binomial coefficients.

## License

This project is licensed under the MIT License.

