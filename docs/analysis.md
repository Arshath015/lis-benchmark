# Analysis of LIS Benchmark Results

The benchmark compares two classic approaches to the Longest Increasing Subsequence
problem:

* **Naive DP** – O(n^2) dynamic programming. It builds an ``dp`` array where each
  entry stores the length of the LIS ending at that position. The double loop
  dominates runtime, leading to quadratic growth.
* **Optimized Patience Sorting** – O(n log n). It maintains a ``tails`` list of
  the smallest possible tail for each subsequence length. Inserting each element
  via binary search yields logarithmic per‑item cost.

From the generated ``results/comparison.md`` we observe that the optimized
variant scales almost linearly with input size, while the naive method exhibits
quadratic growth. Even at modest sizes (n=2000) the speedup exceeds 100×, confirming
the theoretical advantage of the binary‑search strategy.
