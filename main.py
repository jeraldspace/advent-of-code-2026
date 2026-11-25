from pathlib import Path


def part1(data: str) -> None:
    # Implement the first part of the challenge here.
    return None


def part2(data: str) -> None:
    # Implement the second part of the challenge here.
    return None


def main() -> None:
    data = Path(__file__).with_name("input.txt").read_text()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
