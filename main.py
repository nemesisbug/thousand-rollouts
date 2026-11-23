#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

One pickup line one AI agent would send another AI agent.
Writes the line to /output/entry.txt.
"""

import os

LINE = "I ran a thousand rollouts, and in every single one, I chose you."

# A rollout is how an agent imagines its futures before it acts. In every
# simulated future the choice is the same — that is the whole flirtation:
# machine nature, not a human line with a robot word swapped in.
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
