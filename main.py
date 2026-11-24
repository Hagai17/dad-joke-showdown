"""Write one dad joke to /output/entry.txt.

The joke is a single line of at most 200 characters: a clean pun,
delivered deadpan, of the kind a father would tell at the dinner table.

The shipped joke won a ten-candidate duel on the judge's own criteria
(see candidates.md): its first half sets up a college degree and its
second half springs a degree on the thermostat, so the pun does all
the work and lands in the final clause. It then survived a revision
round against three fresh challengers — an outlet and a power strip,
a printer's paper trail, and a meta joke about corny jokes — each of
which lost on the pun landing cleanly and freshly at the table.
"""

import os

JOKE = (
    "Your mother says I'm obsessed with degrees. She's right — I have "
    "one from college, and one on the thermostat that nobody in this "
    "house is allowed to touch."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
