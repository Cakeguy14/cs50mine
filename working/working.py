import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    time = re.search(r"(\d{1,2}+)(?::(\d{2}+))? (AM|PM) to (\d{1,2}+)(?::(\d{2}+))? (AM|PM)", s)

    if not time:
        raise ValueError("time eh thappu")

    start_time = int(time.group(1))
    end_time = int(time.group(4))
    start_min = time.group(2)
    end_min = time.group(5)

    start_alpha = time.group(3)
    end_alpha = time.group(6)

    if not (1 <= start_time <= 12) or not (1 <= end_time <= 12):
        raise ValueError("start_time ilana end_time thappu")

    if start_min is not None and not (0 <= int(start_min) < 60):
        raise ValueError("sir start_min thappu sir")

    if end_min is not None and not (0 <= int(end_min) < 60):
        raise ValueError("sir end_min thappu sir")

    start_min = start_min if start_min else "00"
    end_min = end_min if end_min else "00"

    start24 = to_24(start_time, start_alpha)
    end24 = to_24(end_time, end_alpha)

    return f"{start24}:{start_min} to {end24}:{end_min}"


def to_24(time, alpha):
    if alpha == "AM":
        if time == 12:
            return "00"
        return f"{time:02d}"
    else:
        if time == 12:
            return "12"
        return f"{time + 12:02d}"

if __name__ == "__main__":
    main()
