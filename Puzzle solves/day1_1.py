def password_finder():
    import os
    from pathlib import Path

    root = Path(__file__).parent.parent
    print("Path: ", root)
    puzzle_input = (root / "Puzzle Inputs" / "day1.txt").resolve()
    print("Puzzle Input Path: ", puzzle_input)


    with open(puzzle_input, "r") as file:
        lines = file.readlines()

    print(f"Total number of lines: {len(lines)}")

password_finder()