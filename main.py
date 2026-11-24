"""Office joke entry: writes one line of office comedy to entry.txt."""

import os

TEXT = "Our team voted to make Fridays meeting-free, so the calendar auto-booked a meeting to discuss it."


def validated_text():
    """Enforce the gate: UTF-8, 1-200 characters, one line, not only space."""
    raw = TEXT.encode("utf-8")
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert "\n" not in TEXT and TEXT.strip(), "entry must be a single non-blank line"
    assert raw.decode("utf-8") == TEXT
    return raw


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = validated_text() + b"\n"
    with open(path, "wb") as f:
        f.write(data)
    # Re-read to prove the bytes landed intact.
    with open(path, "rb") as f:
        assert f.read() == data


if __name__ == "__main__":
    main()
