# Discussion.md

## 1. Solutions Considered
- **Naive Scan**: Would read the entire file. Easy but too slow.
- **grep/awk**: Faster than naive but still scans the whole file.
- **Binary Search by Date**: Much more efficient, only scans relevant portion.

## 2. Final Solution Summary
We chose the binary search approach because the log is chronologically sorted and we want to skip large unneeded sections quickly.

## 3. Steps to Run
1. Install Python 3.
2. In your terminal, run:
   ```bash
   cd src
   python extract_logs.py 2024-12-01
