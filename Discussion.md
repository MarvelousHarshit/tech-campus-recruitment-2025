# Discussion.md



# 1. Solutions Considered

# a. Naive Line-by-Line Scan

**Approach**: Iterate over the entire 1 TB file line by line, check the date, and output matches.

Pros: Easy to implement.
Cons: Potentially very slow and resource-heavy. It requires reading the entire file even if you only need a small portion.



# b. Command-Line Tools (grep/awk/etc.)

**Approach**: Leverage system-level utilities to filter by date (e.g., grep "YYYY-MM-DD" file).

Pros: Simple one-liner; native tools in C might be optimized.
Cons: Still reads the entire file. No random access or partial scanning.



# c. Splitting Logs as They Are Generated

**Approach**: If the system could have stored logs in daily or monthly files, retrieval would be trivial (just load the target file).

Pros: Almost instant retrieval for a specific date.
Cons: Requires changing how logs are generated or maintained. Not always feasible if you already have a single large file.



# d. Binary Search by Date (Chosen Approach)

**Approach**: Because the file is chronologically sorted and logs are evenly distributed over days, we can do a binary search at the file-offset level to find the first occurrence of the target date. We then read sequentially until the date changes.

Pros: Minimizes scanning—quickly jumps to the relevant portion of the file, significantly reducing I/O.
Cons: More complex logic to manage file offsets and partial lines.







# 2. Final Solution Summary

We selected the Binary Search by Date approach. Since each log begins with a timestamp in chronological order, we can quickly “jump” to the portion of the file that contains the date in question. Once we find the start of that date, we scan forward until we reach the next day’s logs.

This significantly reduces read time and system overhead for large files because we avoid examining vast sections of data that are guaranteed to be out of our date range.


# 3. Steps to Run

# 1. Set up your environment

Install Python 3 (if it’s not already available).
Ensure you have a large log file available (named test_logs.log or updated in the script if different).



# 2. Download or Clone the Repository

Fork the contest repository, then clone your fork locally.



# 3. Place Your Scripts

Put the final Python script (e.g., extract_logs.py) in the src/ directory.
Make sure to update the LOG_FILE_PATH in the script to point to the actual path of test_logs.log.



# 4. Run the Code

Open a terminal in your src directory and execute:
python extract_logs.py 2024-12-01
Replace 2024-12-01 with the date you need.



# 5. Check the Output

The script creates a file in output/ named output_YYYY-MM-DD.txt containing only the logs from the specified date.

