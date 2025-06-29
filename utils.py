import re

def extract_date_time(text):
    # Extract date in YYYY-MM-DD format
    date_match = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", text)
    date_str = date_match.group(1) if date_match else None

    # Extract time in HH:MM format
    time_match = re.search(r"\b(\d{1,2}:\d{2})\b", text)
    time_str = time_match.group(1) if time_match else None

    if date_str:
        return (date_str, time_str)
    return None
