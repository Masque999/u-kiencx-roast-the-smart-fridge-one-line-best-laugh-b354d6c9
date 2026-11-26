LINE = "My smart fridge judges my midnight snacks out loud, then locks the ice cream drawer and calls it tough love."

# The entry must be exactly one line of 1-160 characters.
assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
assert "\n" not in LINE

import os
assert LINE == LINE.strip(), "line must not have leading or trailing whitespace"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# Read back what was written: a silent partial write must fail loudly.
with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
    assert f.read() == LINE, "entry.txt does not match LINE"
