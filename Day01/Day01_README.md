# Day 01 – My Data Science Journey

## What I learned today
Today marked the official start of my structured Data Science learning journey, following the 80/20 principle.  
I began with warm-up Python challenges to assess my current skills, then moved into list and dictionary comprehensions, and finally touched on NumPy basics.

---

## My thought process
- I approached each problem step-by-step, writing a straightforward solution first.
- I prioritized correctness before optimization.
- After getting the right output, I explored more concise and Pythonic ways to solve them.
- I actively reflected on mistakes and learned from feedback, especially on comprehension order.

---

## Mistakes I made & lessons learned
1. **Nested comprehensions** – I initially tried using `and` between loops, which isn’t valid syntax. I learned that comprehensions are ordered by loops first, then conditions, and `and` is not used to chain loops.
2. **Hardcoding checks** – For filtering names with 'a', I looped over characters instead of using `.startswith()`; I learned cleaner methods.
3. **Overthinking simple problems** – Some problems were simpler than I first assumed.
4. **NumPy shapes** – I reinforced my understanding of `shape`, `ndim`, `dtype`, and `astype`.
5. **Identity matrix** – Learned what it is and why it’s used in linear algebra (multiplicative identity).

---

## Aha moments
- Comprehensions are both a **loop** and a **filter** in one expression.
- NumPy operations are vectorized — they apply to the whole array without explicit loops.
- `np.eye()` creates the identity matrix, which is crucial for matrix multiplication logic.

---

## Tomorrow’s plan
- Continue with NumPy Arrays (indexing, slicing, advanced selection).
- Practice more vectorized operations.
- Begin with basic statistical functions in NumPy.

---

## Day Summary Table

| Problem # | Topic | Difficulty | Status |
|-----------|-------|------------|--------|
| 1         | Filter Even Numbers | Easy | ✅ Solved |
| 2         | Filter Dict by Value | Easy | ✅ Solved |
| 3         | Count Words | Easy | ✅ Solved |
| 4         | FizzBuzz | Easy | ✅ Solved |
| 5         | Names Starting with A | Medium | ✅ Solved |
| 6         | List Comprehensions (Squares) | Easy | ✅ Solved |
| 7         | Filter Words > 3 Letters | Easy | ✅ Solved |
| 8         | Dict Comprehension (Cubes) | Easy | ✅ Solved |
| 9         | Names Length Dict | Easy | ✅ Solved |
| 10        | Flatten Matrix | Medium | ✅ Solved |
| 11        | Nested Comprehension Transform | Medium | ✅ Solved |
| 12        | Cartesian Pairs w/ Condition | Medium | ✅ Solved |
| 13        | Convert List of Lists to Dict | Easy | ✅ Solved |
| 14        | NumPy Basics (`arange`, `reshape`, attributes) | Medium | ✅ Solved |
| 15        | Identity Matrix (`np.eye`) | Medium | ✅ Solved |
