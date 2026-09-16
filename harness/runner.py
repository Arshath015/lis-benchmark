"""Benchmark harness for LIS implementations.

Runs both the naive and optimized variants on a series of input sizes and stores
the wall‑clock time in milliseconds. Results are written to ``results/comparison.md``.
"""

import time
import random
from pathlib import Path
from typing import List, Tuple

from implementations.naive import NaiveLIS
from implementations.optimized import OptimizedLIS

RESULTS_PATH = Path(__file__).resolve().parents[1] / "results" / "comparison.md"

def generate_sequence(n: int, seed: int = 0) -> List[int]:
    rnd = random.Random(seed)
    return [rnd.randint(0, n * 10) for _ in range(n)]

def time_algorithm(alg, seq: List[int]) -> float:
    start = time.perf_counter()
    alg.compute(seq)
    end = time.perf_counter()
    return (end - start) * 1000.0  # ms

def run_benchmarks(sizes: List[int]) -> List[Tuple[int, float, float]]:
    naive = NaiveLIS()
    opt = OptimizedLIS()
    results = []
    for n in sizes:
        seq = generate_sequence(n, seed=n)
        t_naive = time_algorithm(naive, seq)
        t_opt = time_algorithm(opt, seq)
        results.append((n, t_naive, t_opt))
    return results

def write_results(results: List[Tuple[int, float, float]]) -> None:
    header = "| Size | Naive (ms) | Optimized (ms) | Speedup |\n|---|---|---|---|\n"
    lines = [header]
    for size, t_naive, t_opt in results:
        speedup = t_naive / t_opt if t_opt > 0 else float('inf')
        lines.append(f"| {size} | {t_naive:.2f} | {t_opt:.2f} | {speedup:.2f} |\n")
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(''.join(lines))

if __name__ == "__main__":
    sizes = [100, 500, 1000, 2000]
    results = run_benchmarks(sizes)
    write_results(results)
