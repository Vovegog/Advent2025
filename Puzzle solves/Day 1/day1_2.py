def password_finder():
    from pathlib import Path

    dial: int = 50
    zero_count: int = 0
    dial_nums: int = 100

    cwd = Path(__file__)
    puzzle_input = (cwd.parent.parent.parent/"Puzzle Inputs"/"day1.txt")

    with open(puzzle_input, "r") as file:
        lines = file.readlines()

    for line in lines:
        direction: str = line[0]
        amount: int = int(line[1:])

        if direction == "L":
            for _ in range(amount):
                dial -= 1
                if dial < 0:
                    dial = dial_nums - 1
                if dial == 0:
                    zero_count += 1
        elif direction == "R":
            for _ in range(amount):
                dial += 1
                if dial >= dial_nums:
                    dial = 0
                if dial == 0:
                    zero_count += 1

        


    print(f"Total number of lines: {len(lines)}")
    print(f"Number of times dial hit zero: {zero_count}")

password_finder()