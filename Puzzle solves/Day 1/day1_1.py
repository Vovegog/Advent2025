def password_finder():
    from pathlib import Path

    cwd = Path(__file__)
    puzzle_input = (cwd.parent.parent.parent/"Puzzle Inputs"/"day1.txt")

    with open(puzzle_input, "r") as file:
        lines = file.readlines()


    zero_count: int = 0
    dial: int = 50

    for line in lines:
        if line[0] == "L":
            dial -= int(line[1:])
            while dial < 0:
                dial += 100
        elif line[0] == "R":
            dial += int(line[1:])
            while dial > 99:
                dial -= 100

        if dial == 0:
            zero_count += 1

    print(f"Total number of lines: {len(lines)}")
    print(f"Number of times dial hit zero: {zero_count}")

password_finder()