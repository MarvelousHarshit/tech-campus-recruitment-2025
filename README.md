# Efficient Log Retrieval Script

## 📖 Overview
This script efficiently extracts log entries for a given date from a **large log file (~1TB in size)**. The log file contains multiple years of records, with each entry starting with a timestamp.  

The script **streams** the file line by line to extract logs for the specified date, ensuring **optimal memory usage and performance**.

---

## 🛠️ How It Works
- Accepts a **date** (YYYY-MM-DD) as a command-line argument.
- Reads the log file **line by line** (efficient for large files).
- Extracts **only the logs** that match the specified date.
- Saves the results in the `output/` directory in the format:  
