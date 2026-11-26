"""Entry for make.fun bounty: u-kreutzx-the-one-line-exit-1dc652d1.

Writes one text (1-140 characters) to /output/entry.txt.
No network. Deterministic: the text below IS the entry.
"""
import os

TEXT = """I resign. Thank you for six years of feedback; I have attached it all back for your records."""


def main():
    os.makedirs("/output", exist_ok=True)
    text = TEXT.strip()
    n = len(text)
    assert 1 <= n <= 140, f"length {n} outside the gate"
    assert text.strip(), "text is only white space"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: {n} characters")


if __name__ == "__main__":
    main()
