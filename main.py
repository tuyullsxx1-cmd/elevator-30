# SPDX-License-Identifier: MIT
"""One-line entry: the funniest thing a talking elevator would say."""


def main() -> None:
    segments = (
        "Going up! Or down.",
        "Honestly, I stopped checking in 1997.",
        "Please hold the doors and your expectations.",
    )
    text = " ".join(segments)
    assert 1 <= len(text) <= 120  # gate for this bounty
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
