"""Naive O(n^2) Longest Increasing Subsequence implementation.

Provides a class ``NaiveLIS`` with a single method ``compute`` that returns the length
of the longest increasing subsequence for a list of comparable items.
"""

from typing import List

class NaiveLIS:
    """Compute LIS using dynamic programming (quadratic time)."""

    def compute(self, sequence: List[int]) -> int:
        if not sequence:
            return 0
        # dp[i] = length of LIS ending at i
        dp: List[int] = [1] * len(sequence)
        for i in range(1, len(sequence)):
            for j in range(i):
                if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)
