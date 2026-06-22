# ⚙️ How It Works: GitHub Contribution Graph Backdating

This document explains the mathematics, date calculations, and Git properties used to paint the name **"NAMAN"** on the 2019 GitHub Contribution Graph.

---

## 1. The GitHub Grid System

GitHub displays your contributions in a grid:
* **Rows (Y-axis)**: Represents the days of the week, starting with **Sunday (row 0)** and ending with **Saturday (row 6)**.
* **Columns (X-axis)**: Represents the weeks of the year, spanning **53 weeks (columns 0 to 52)**.

A single pixel in the graph is represented by its coordinate `(row, col)` where:
$$0 \le \text{row} \le 6$$
$$0 \le \text{col} \le 52$$

---

## 2. Letter Layout & Centering Calculations

To render **"NAMAN"** cleanly and symmetrically, we designed a character matrix for each letter with a height of 7 pixels (covering all days of the week) and a width of 5 pixels.

### Character Matrices:
* **`N`**: Vertical bars on columns 0 and 4, with a diagonal stepping down from top-left to bottom-right.
* **`A`**: An A-frame arch with a horizontal crossbar on row 3.
* **`M`**: Vertical bars on columns 0 and 4, with an inner V-shape.

### Centering Math:
* Total width of the word:
  $$\text{Width} = (5 \text{ letters} \times 5 \text{ pixels}) + (4 \text{ spaces} \times 1 \text{ pixel}) = 29 \text{ columns}$$
* Centering alignment:
  $$\text{Margin} = \frac{53 - 29}{2} = 12 \text{ columns on each side}$$

Thus, the word starts at column index **12** and ends at column index **40** (inclusive).

---

## 3. Backdating Date Calculations

GitHub plots contribution pixels on the graph according to the date of the commit. To backdate commits to specific cells in 2019, we calculated the precise calendar date for each `(row, col)` coordinate:

1. **Find the first day of the graph**:
   January 1, 2019 was a **Tuesday**. Since the calendar week on GitHub always begins on Sunday, the Sunday of that first week was **December 30, 2018**.
   
   $$\text{Base Sunday} = \text{2018-12-30}$$

2. **Compute specific dates**:
   To find the date for any coordinate `(row, col)` on the grid, we add the total offset days to our base Sunday:
   
   $$\text{Target Date} = \text{Base Sunday} + (\text{col} \times 7) + \text{row}$$

* For example, the top-left pixel of our first letter 'N' at `(row 0, col 12)` corresponds to:
  $$\text{2018-12-30} + (12 \times 7) + 0 = \text{2018-12-30} + 84 \text{ days} = \text{2019-03-24}$$ (Sunday)
* The bottom-right pixel of the final 'N' at `(row 6, col 40)` corresponds to:
  $$\text{2018-12-30} + (40 \times 7) + 6 = \text{2018-12-30} + 286 \text{ days} = \text{2019-10-12}$$ (Saturday)

All generated dates fall safely within the calendar year 2019.

---

## 4. Setting the Backdate in Git

When you run `git commit`, Git records two different timestamps:
1. **Author Date**: When the code was originally written.
2. **Committer Date**: When the commit was applied to the repository.

GitHub's contribution graph relies on the **Author Date**. However, to ensure maximum compatibility and avoid mismatch issues, the script overrides both dates using Git environment variables before performing the commit:

```python
import os
import subprocess

# Set environment variables for the subprocess
env = os.environ.copy()
env["GIT_AUTHOR_DATE"] = "2019-03-24T12:00:00"
env["GIT_COMMITTER_DATE"] = "2019-03-24T12:00:00"

# Make the commit
subprocess.run(
    ["git", "commit", "--allow-empty", "-m", "Contribution Art Commit"],
    env=env
)
```

---

## 5. Contribution Color Depth

GitHub uses four levels of green to show contribution density, calculated dynamically relative to your daily average:
1. **Light Green** (Low activity)
2. **Medium Green** (Medium activity)
3. **Dark Green** (High activity)
4. **Deepest Green** (Very high activity)

To guarantee that the text is sharp and uniformly printed in the **deepest green** color, the script creates **12 commits** for every active coordinate, which is well above the usual daily threshold for the dark hue.
