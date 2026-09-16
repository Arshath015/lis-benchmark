"""Optimized O(n log n) Longest Increasing Subsequence implementation.

The class ``OptimizedLIS`` maintains a ``tails`` list where ``tails[i]`` is the
smallest possible tail value of an increasing subsequence of length ``i+1``.
Binary search (via ``bisect_left``) places each element in ``tails`` in O(log n).
"""

from bisect import bisect_left
from typing import List

class OptimizedLIS:
    """Compute LIS using patience sorting technique (binary‑search)."""

    def compute(self, sequence: List[int]) -> int:
        if not sequence:
            return 0
        tails: List[int] = []
        for x in sequence:
            # Find insertion point
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(tails)
