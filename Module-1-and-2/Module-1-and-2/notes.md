# Study Notes & Assignment Trackers (Modules 1 & 2)

Here are my personal notes and thoughts as I work through the first two modules of the course. Keeping track of how I solved things and what clicked for me.

---

## 1. Magic Squares
* **3x3 Magic Square:** 
  * The goal is to arrange numbers from 1 to 9 so every row, column, and diagonal adds up to 15.
* **Narrowing the Search:** 
  * At first, it feels like you have to check thousands of combinations (9! options). But if you look at the math closely, you realize the center cell has to be 5 because it shares the most lines. Once you lock 5 in the middle, the whole puzzle becomes way easier to solve.
* **Multiplicative Magic Squares:** 
  * Same idea, but instead of adding numbers, you multiply them. Every row, column, and diagonal must give the exact same product. Makes you think a lot about prime factorization.

---

## 2. Integer Linear Combinations & Coin Puzzles
* **Different People Have Different Coins:** 
  * *Notes to self:* When you are dealing with specific coin values (like 7 and 13), you quickly realize you can't form every single amount. Some numbers are just out of reach.
  * **How to figure out the limit:** For two coprime numbers a and b, the biggest number you can never form is `(a * b) - a - b`.
  * *Example:* If the coins are 7 and 13: `(7 * 13) - 7 - 13 = 91 - 20 = 71`. 
  * So, anything bigger than 71 is totally reachable, but 71 and a few specific numbers below it are impossible. Good shortcut to keep in mind.
* **Free Accommodation:** 
  * Working through room combinations and figuring out step-by-step how to reach target integer values.
* **Paths in a Graph ("Is there..."):** 
  * Turning weird puzzle rules into a simple graph so I can actually see if a valid path exists between nodes.

---

## 3. Optimality & Computer Search (Overview)
* **Subset Optimality:** 
  * Figuring out how to pick the biggest possible subset while following strict rules (like no two numbers adding up to 100, or avoiding a number and its double).
* **Chessboard Optimality:** 
  * Trying to pack as many non-attacking pieces (Rooks, Knights, Bishops) onto a board as possible. Using grid patterns makes it much simpler to prove the maximum limit.
* **Computer Search & Backtracking:** 
  * Moving away from brute force (which takes forever) and using smart backtracking for things like N-Queens and the 16 Diagonals puzzle. Pruning dead ends early saves so much time.
