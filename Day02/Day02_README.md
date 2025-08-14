# Day 02 – NumPy Indexing, Boolean Masks, Broadcasting (Full Day)

## What I learned today (in my words)
I practiced NumPy array creation, slicing (1D and 2D), boolean indexing, conditional assignment, fancy indexing vs rectangular selections, and broadcasting along rows and columns. I also used `linspace` to generate smooth ranges for sine waves and reshaped arrays for structured outputs. Finally, I tied these together with aggregation patterns I’ll use tomorrow (mean/std per row, column sums).

## My thought process
- Write a working version first, then make it concise and NumPy-idiomatic.
- Prefer masks and broadcasting instead of loops.
- Use `keepdims=True` for row/column stats when I need to broadcast them back.

## Mistakes I made & lessons learned
- Boolean indexing like `arr[mask]` creates a copy; in-place edits require chaining masks directly on the original.
- Two index arrays of equal length perform **element-wise pairing**; for rectangular submatrices I should use slices or `np.ix_`.
- Broadcasting works right-to-left on shapes; dimensions must either match or be 1.

## Aha moments
- `np.ix_` is the clean way to get all combinations of chosen rows and columns.
- Broadcasting a `(rows,1)` vector scales rows; broadcasting a `(cols,)` or `(1,cols)` vector scales columns.
- Reshaping changes the view, not the values—stats (mean/std) are unaffected by reshape.

## Tomorrow’s plan
- Aggregations across axes in practice (`sum`, `mean`, `std`, `min`, `max`, `arg*`).
- Row-wise z-score standardization and a column-replacement mini task (data cleaning demo).
- More boolean logic with `.any()` / `.all()` for dataset filtering.

## Day Summary Table
| # | Topic | Difficulty | Status |
|---|-------|------------|--------|
| 1 | `np.array` / `np.arange` → 2D, inspect | Easy | ✅ |
| 2 | `np.arange(10,31,5)` | Easy | ✅ |
| 3 | `np.linspace(5,50,7)` | Easy | ✅ |
| 4 | `sin(linspace(0,2π,100))` | Easy | ✅ |
| 5 | `linspace(10,100,20)` + reshape 4×5 + step/mean/std | Medium | ✅ |
| 6 | `sin(linspace(0,4π,200))` + reshape 20×10 | Medium | ✅ |
| 7 | 1D slicing (evens, every 3rd) | Easy | ✅ |
| 8 | 2D slicing (3×5), last row reversed | Medium | ✅ |
| 9 | Boolean filter 10< x <18 | Easy | ✅ |
|10 | Conditional assign subset (5..15 & <10 → -1) | Medium | ✅ |
|11 | 4×5 10..29: even→0; odd>20→99 | Medium | ✅ |
|12 | Mean-based replacement (<mean→-5, >mean→5) | Easy | ✅ |
|13 | Fancy indexing drill (pairing vs `np.ix_`) | Medium | ✅ |
|14 | Mixed slicing + broadcasting quiz (verified) | Medium | ✅ |
|15 | Broadcasting check (A*B, A*C, B*C) | Medium | ✅ |
