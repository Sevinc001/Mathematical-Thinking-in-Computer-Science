# Module 1 & 2: Proofs, Puzzles, Optimality, Magic Squares & Computer Search

This repository folder contains theoretical breakdowns, teacher notes, graded assignment summaries, and problem-solving strategies for **Modules 1 and 2** of the *Mathematical Thinking in Computer Science* course.

---

## 📚 Table of Contents
1. [Module 1: Proofs & Existence](#-module-1-proofs--existence)
2. [Module 2: Magic Squares, Optimality & Computer Search](#-module-2-magic-squares-optimality--computer-search)

---

## 🧩 Module 1: Proofs & Existence

### 1. Proof Strategies & Invariants
* **Proof by Example & Impossibility Proofs:** Constructing explicit examples vs. using logical invariants to prove a solution cannot exist.
* **The Mutilated Chessboard Puzzle:** Proving why removing two opposite corners of the same color makes domino tiling impossible (invariant: equal numbers of black and white tiles required).
* **Existence & Shapes:** Splitting octagons and shapes into congruent parts.

---

## 🔮 Module 2: Magic Squares, Optimality & Computer Search

### 1. Magic Squares & Linear Combinations
* **$3 \times 3$ Magic Squares:**
  * *Concept:* Arranging numbers $1$ to $9$ in a $3 \times 3$ grid so that every row, column, and main diagonal sums to $15$.
  * *Narrowing the Search:* Using algebraic logic to prove the central tile must always be $5$.
* **Multiplicative Magic Squares:** Grids where the product of elements in rows, columns, and diagonals are equal.
* **Integer Linear Combinations & Diophantine Equations:**
  * **Puzzle: Different People Have Different Coins:** Solving coin exchange problems using greatest common divisors (GCD) and linear combinations.
  * **Puzzle: Free Accommodation:** Determining achievable values through linear combinations of integers.
* **Graph Logic ("Paths in a Graph" / "Is there..."):** Translating existence puzzles into graph traversals.

---

### 2. Optimality Problems
* **Number Theory & Subset Optimality:**
  * **Maximum Number of Two-Digit Integers:** Finding maximal subsets under parity or divisibility rules.
  * **Subset without $x$ and $100-x$:** Finding the maximum size of a set where no two elements add up to $100$.
  * **Subset without $x$ and $2x$:** Optimization logic to select the maximum elements without containing any element and its double.
* **Chessboard Optimality (Placement Constraints):**
  * **Rooks on a Chessboard:** Maximum non-attacking rooks on an $N \times N$ board is $N$.
  * **Knights on a Chessboard:** Maximum non-attacking knights on an $N \times N$ board using monochromatic grid partitioning ($\lceil N^2 / 2 \rceil$).
  * **Bishops on a Chessboard:** Maximum non-attacking bishops on an $N \times N$ board ($2N - 2$).

---

### 3. Computer Search & Backtracking Algorithms
* **N-Queens Puzzle:**
  * *Problem:* Placing $N$ non-attacking queens on an $N \times N$ chessboard.
  * *Brute-Force Search:* Generating all $N!$ permutations and testing validity.
  * *Backtracking Solution:* Building partial solutions row-by-row and pruning invalid subtrees early.
* **16 Diagonals Puzzle:**
  * Placing $16$ non-intersecting diagonals on a $5 \times 5$ grid using recursive backtracking search.
* **8-Queens Solution Counting:** Calculating all $92$ distinct valid arrangements for $N=8$.
