# Futsal Action Efficiency Index

**FAEI (Futsal Action Efficiency Index)** is a universal mathematical model for evaluating a futsal player's match contribution based on both attacking and defensive actions.

It combines:
- **action quality** (success ratio),
- **action volume** (number of attempts, with logarithmic scaling),
- **action importance** (weights per action type),
- **and a volume cap** to prevent inflation from quantity alone.

---

## Core metrics

**Attack**
- `A_DUALS` — attacking duels
- `A_SHOTS` — shots and finishes
- `A_DRIBBLES` — dribbles
- `A_PROGRESSIVE_PASS` — progressive or key passes

**Defense**
- `D_DUALS` — defensive duels / pressing
- `D_BLOCKED_SHOT` — blocked shots or passes
- `D_TRUNCATED_BALL` — intercepted or cut balls
- `D_PROGRESSIVE_PASS` — progressive pass from defense

---

## Example

```python
from faei import FAEICalculator

actions = {
    "A_DUALS": {"attempts": 3, "success": 2},
    "A_SHOTS": {"attempts": 6, "success": 3},
    "A_DRIBBLES": {"attempts": 2, "success": 2},
    "A_PROGRESSIVE_PASS": {"attempts": 4, "success": 3},
    "D_DUALS": {"attempts": 5, "success": 4},
    "D_BLOCKED_SHOT": {"attempts": 1, "success": 1},
    "D_TRUNCATED_BALL": {"attempts": 2, "success": 1},
    "D_PROGRESSIVE_PASS": {"attempts": 1, "success": 1},
}

calc = FAEICalculator()
result = calc.calc(actions)
print(result)
# {'fai_attack': 4.123, 'fai_defense': 3.557, 'fai_total': 7.68}
```
