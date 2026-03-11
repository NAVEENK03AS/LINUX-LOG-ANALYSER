import sys

def analyze_log(file):

    with open(file,"r") as f:
        lines = f.readlines()

    error_count = 0
    warning_count = 0

    for line in lines:
        if "error" in line.lower():
            error_count += 1
        if "warning" in line.lower():
            warning_count += 1

    print("Total lines:", len(lines))
    print("Errors:", error_count)
    print("Warnings:", warning_count)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py logfile")
    else:
        analyze_log(sys.argv[1])
