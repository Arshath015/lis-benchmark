# Longest Increasing Subsequence Benchmark Report

![GitHub last commit](https://img.shields.io/github/last-commit/user/lis-benchmark)
![License](https://img.shields.io/badge/license-MIT-blue)

A concise benchmark suite that measures and compares a naive O(n^2) and an optimized O(n log n) implementation of the Longest Increasing Subsequence (LIS) algorithm.

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Theoretical Background](#theoretical-background)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Analysis Document](#analysis-document)
- [Testing](#testing)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [License](#license)

## Overview
This repository contains two independent LIS implementations and a lightweight
benchmark harness. Results are stored in ``results/comparison.md`` and a short
technical analysis lives in ``docs/analysis.md``.

## Tech Stack
- Python 3.9+
- Standard library only (``bisect``, ``time``, ``random``)
- ``pytest`` for testing

## Architecture
```
text
lis-benchmark/
├─ implementations/
│  ├─ naive.py          # O(n^2) DP implementation
│  └─ optimized.py     # O(n log n) binary‑search implementation
├─ harness/
│  └─ runner.py        # Benchmark driver, writes results/comparison.md
├─ tests/
│  ├─ test_naive.py    # pytest suite for NaiveLIS
│  └─ test_optimized.py# pytest suite for OptimizedLIS
├─ results/
│  └─ comparison.md    # Tabular benchmark output
└─ docs/
   └─ analysis.md      # Narrative on performance observations
```
```

## Theoretical Background
The Longest Increasing Subsequence problem asks for the maximum‑length subsequence
of a sequence of numbers where each element is strictly greater than its predecessor.

A classic dynamic‑programming solution runs in O(n^2) time by maintaining an array
``dp[i]`` that records the length of the LIS ending at position ``i``. For each
``i`` we examine all previous ``j < i`` and update ``dp[i]`` when ``seq[j] < seq[i]``.

A more sophisticated approach, often called *patience sorting*, achieves O(n log n)
by keeping a list ``tails`` where ``tails[k]`` is the smallest possible tail value
for an increasing subsequence of length ``k+1``. Inserting a new element uses binary
search (``bisect_left``) to locate the appropriate position, guaranteeing logarithmic
updates. The final length of ``tails`` equals the LIS length.

Both algorithms return the same result, but their asymptotic complexities differ
significantly, which this benchmark quantifies.

## Installation
```bash
git clone https://github.com/user/lis-benchmark.git
cd lis-benchmark
pip install -r requirements.txt  # only pytest is required for testing
```

## Usage
Run the benchmark harness to generate fresh results:
```bash
python -m harness.runner
```
Open ``results/comparison.md`` to view the timing table.

## API Reference
### class NaiveLIS
- ``compute(sequence: List[int]) -> int``: Returns length of LIS using O(n^2) DP.

### class OptimizedLIS
- ``compute(sequence: List[int]) -> int``: Returns length of LIS using O(n log n) binary‑search.

## Analysis Document
The performance discussion is documented in ``docs/analysis.md``.

## Testing
```bash
pytest -q
```
The test suite validates both implementations on empty input, a simple mixed
sequence, and a strictly descending sequence (edge case).

## Limitations
- Only integer sequences are demonstrated; the implementations rely on the
  ``<`` operator and thus work for any comparable type.
- Benchmark runs are single‑threaded and measure wall‑clock time only; more
  rigorous profiling is out of scope.

## Roadmap
- Add support for retrieving the actual LIS elements, not just its length.
- Include multi‑core benchmarking and statistical confidence intervals.
- Extend to handle very large inputs using NumPy for vectorised preprocessing.

## License
MIT License
