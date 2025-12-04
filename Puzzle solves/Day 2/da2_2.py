from pathlib import Path

class ID_verifier:
    def __init__(self) -> None:
        self.sum_ids: int = 0

    def read_input(self, file_path) -> list[str]:
        with open(file_path, 'r') as file:
            # Input is given as one single line, convert to list by splitting on ","
            ids = [str(id_str) for id_str in file.read().strip().split(",")]
        return ids

    def verify_id(self, ids: list[str]) -> int:
        import re
        pattern_full = re.compile(r'^(\d+)\1+$')  # whole number is X repeated Y times

        for id_str in ids:
            left_str, right_str = [p.strip() for p in id_str.split("-")]
            left = int(left_str)
            right = int(right_str)

            for num in range(left, right + 1):
                num_str = str(num)
                if pattern_full.match(num_str):
                    self.sum_ids += num

        return self.sum_ids


if __name__ == "__main__":
    puzzle_input = Path(__file__).parent.parent.parent / "Puzzle Inputs" / "day2.txt"
    verifier = ID_verifier()
    id_list = verifier.read_input(puzzle_input)
    result = verifier.verify_id(id_list)
    print(f"Result: {result}")