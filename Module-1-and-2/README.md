# Module 1 & 2: Proofs, Puzzles, Optimality, Recursion & Logic

This comprehensive folder contains detailed study notes, instructor insights, puzzle breakdowns, and practical Python implementations for the first two combined modules.

---

## 🚀 Quick Navigation
1. [Module 1: Proofs, Puzzles & Computer Search](#-module-1-proofs-puzzles--computer-search)
2. [Module 2: Recursion, Magic Squares & Algorithms](#-module-2-recursion-magic-squares--algorithms)

---

## 🧩 Module 1: Proofs, Puzzles & Computer Search

### 1. Proof Strategies & Impossibility Puzzles
* **The Mutilated Chessboard Puzzle:** 
  * *Instructor Note:* Classic example of an **invariant**. If you remove two opposite corner squares of a chessboard, they are always the same color. Since a single domino always covers one black and one white square, covering the remaining 62 squares with 31 dominoes becomes mathematically impossible.
* **Grid Splitting & Octagon Puzzles:** Analyzing valid and invalid ways to divide geometric shapes into congruent parts.

### 2. Computer Search & Backtracking (Python Projects)
* **N-Queens Puzzle:** 
  * *Concept:* Placing $N$ non-attacking queens on an $N \times N$ chessboard.
  * *Approach:* Moving from naive brute-force permutations to optimized recursive **backtracking** algorithms to prune invalid branches early.
* **16 Diagonals Puzzle:** 
  * *Concept:* Grid-based recursive search ensuring diagonals do not overlap or form unintended loops.

---

## 🔮 Module 2: Recursion, Magic Squares & Algorithms

### 1. Magic Squares & Integer Linear Combinations
* **The Magic Square Puzzle:** 
  * *Concept:* Arranging numbers such that the sums in rows, columns, and diagonals are equal. Exploring multiplicative magic squares and integer linear combinations (e.g., coin exchange problems like 7-florin and 13-florin denominations).

### 2. Recursion & Mathematical Induction
* **Classic Puzzles:**
  * **Hanoi Towers:** The quintessential recursive problem breaking down $N$ disks into sub-problems of $N-1$.
  * **Number Guessing & Local Maximums:** Finding optimal strategies using divide-and-conquer logic.
* **Induction Highlights:** Arithmetic series, plane coloring, compound interest, and strengthening inductive hypotheses.

### 3. Logic, Counterexamples & Pigeonhole Principle
* **"Always Prime" Polynomials:** Exploring why checking finite examples (like Euler's $n^2 - n + 41$) is never enough for a universal proof without rigorous algebraic or counterexample analysis.
* **Pigeonhole Principle:** Distributing items into boxes, antimagic squares, and handshakes principles.
