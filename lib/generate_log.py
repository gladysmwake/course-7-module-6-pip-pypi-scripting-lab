from datetime import datetime
import os


def generate_log(data):
    """
    Generate a timestamped log file from a list of log entries.

    Args:
        data (list): A list of log entry strings to write to the file.

    Returns:
        str: The filename of the generated log file.

    Raises:
        ValueError: If data is not a list.
    """
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)
