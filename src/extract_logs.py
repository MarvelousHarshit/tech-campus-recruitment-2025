import sys
import os

LOG_FILE_PATH = "../test_logs.log"  # Change if your log file is elsewhere
OUTPUT_DIR = "../output"            # Directory for output files

def parse_date_from_line(line):
    """
    Extract 'YYYY-MM-DD' date string from a log line.
    Assumes each log line starts with 'YYYY-MM-DD HH:MM:SS'.
    """
    return line[:10]

def compare_dates(line_date, target_date):
    """
    Compare two date strings in 'YYYY-MM-DD' format.
    Returns -1 if line_date < target_date,
             0 if line_date == target_date,
             1 if line_date > target_date.
    """
    if line_date < target_date:
        return -1
    elif line_date > target_date:
        return 1
    else:
        return 0

def find_first_occurrence(f, target_date):
    """
    Use binary search to find the byte offset of the first log line
    for 'target_date' in the file 'f'.
    If no occurrence is found, returns the file size.
    """
    low, high = 0, os.fstat(f.fileno()).st_size
    result_offset = high

    while low < high:
        mid = (low + high) // 2
        f.seek(mid)

        # Move to the start of the next line
        f.readline()

        if f.tell() >= os.fstat(f.fileno()).st_size:
            break

        line = f.readline()
        if not line:
            break

        line_date = parse_date_from_line(line)
        cmp_res = compare_dates(line_date, target_date)

        if cmp_res >= 0:
            # line_date >= target_date
            result_offset = f.tell() - len(line)
            high = mid
        else:
            # line_date < target_date
            low = mid + 1

    return result_offset

def extract_logs_for_date(target_date):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_file_path = os.path.join(OUTPUT_DIR, f"output_{target_date}.txt")

    with open(LOG_FILE_PATH, "r", encoding="utf-8", errors="replace") as f_in, \
         open(output_file_path, "w", encoding="utf-8") as f_out:

        first_offset = find_first_occurrence(f_in, target_date)
        f_in.seek(first_offset)

        while True:
            line = f_in.readline()
            if not line:
                break
            line_date = parse_date_from_line(line)
            if line_date == target_date:
                f_out.write(line)
            else:
                break

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    target_date = sys.argv[1].strip()
    extract_logs_for_date(target_date)
    print(f"Logs for {target_date} have been written to output/output_{target_date}.txt")

if __name__ == "__main__":
    main()
</details>
