def password_finder(dial: int = 50, zero_count: int = 0, dial_nums: int = 100):
    from pathlib import Path

    cwd = Path(__file__)
    puzzle_input = (cwd.parent.parent/"Puzzle Inputs"/"day1.txt")

    with open(puzzle_input, "r") as file:
        lines = file.readlines()

    for line in lines:
        if line[0] == "L":
            

        if dial == 0:
            zero_count += 1

    print(f"Total number of lines: {len(lines)}")
    print(f"Number of times dial hit zero: {zero_count}")

password_finder()