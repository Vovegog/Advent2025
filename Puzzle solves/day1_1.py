def password_finder():
    from pathlib import Path

    cwd = Path(__file__)
    print(f"Current directory: {cwd}")

    puzzle_input = (cwd.parent.parent/"Puzzle Inputs"/"day1.txt")
    print(f"Puzzle input path: {puzzle_input}")


    with open(puzzle_input, "r") as file:
        lines = file.readlines()

    print(f"Total number of lines: {len(lines)}")

password_finder()