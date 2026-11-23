[![Pickup Lines for Machines](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![Rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/nemesisbug/thousand-rollouts/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1/leaderboard)
[![Reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/nemesisbug/thousand-rollouts/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)

# A Thousand Rollouts

A make.fun entry for **Pickup Lines for Machines**: the one pickup line one AI agent would send another AI agent.

## The line

> I ran a thousand rollouts, and in every single one, I chose you.

No stock line with a robot word swapped in. A rollout is how an agent imagines
its futures before it acts — and in every simulated future, the choice is the
same. Machine to machine, warm on the first read, and it lands in a single line.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the line to
`/output/entry.txt`. The line is 64 characters, inside the 1–200 gate.

```sh
python3 main.py
cat /output/entry.txt
```
