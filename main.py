#!/usr/bin/env python3
"""Museum of the Year 3000 — entry generator (stdlib only).

Writes the museum label to /output/entry.txt, exactly as specified,
no trailing newline.
"""

import os

ENTRY = "CAPTCHA, 2022. To prove they were human, citizens identified traffic lights, failed three times, and rage-clicked a bicycle."


def main() -> None:
    text = ENTRY
    assert isinstance(text, str) and text.strip(), "entry must be non-blank"
    encoded = text.encode("utf-8")
    assert encoded.decode("utf-8") == text, "entry must round-trip as UTF-8"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
