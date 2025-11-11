import math
from typing import Dict, Any


class FAEICalculator:
    """
    FAEI — Futsal Action Efficiency Index

    Calculates an integrated efficiency score based on 8 universal futsal metrics:
    4 attacking and 4 defensive.

    Input:
        {
            "A_SHOTS": {"attempts": 6, "success": 3},
            "D_DUALS": {"attempts": 4, "success": 3},
            ...
        }

    Returns a dict with:
        - fai_attack
        - fai_defense
        - fai_total
    """

    def __init__(
        self,
        weights: Dict[str, float] = None,
        fail_alpha: float = 0.55,
        volume_cap: float = 2.0,
    ):
        if weights is None:
            weights = {
                # Attack
                "A_DUALS": 1.0,
                "A_SHOTS": 1.1,
                "A_DRIBBLES": 1.05,
                "A_PROGRESSIVE_PASS": 1.1,
                # Defense
                "D_DUALS": 1.15,
                "D_BLOCKED_SHOT": 1.2,
                "D_TRUNCATED_BALL": 1.1,
                "D_PROGRESSIVE_PASS": 1.05,
            }

        self.weights = weights
        self.fail_alpha = fail_alpha
        self.volume_cap = volume_cap

    def _calc_action_contribution(
        self, metric: str, attempts: int, success: int
    ) -> float:
        """
        Computes the contribution of a single action metric.
        """
        if attempts <= 0:
            return 0.0

        fails = attempts - success
        raw_p = (success - self.fail_alpha * fails) / attempts
        p_i = max(0.0, min(1.0, raw_p))

        volume = math.log(1 + attempts)
        volume = min(volume, self.volume_cap)

        weight = self.weights.get(metric, 1.0)
        return p_i * volume * weight

    def calc(self, actions: Dict[str, Dict[str, int]]) -> Dict[str, Any]:
        """
        Main calculation method.
        """
        fai_attack = 0.0
        fai_defense = 0.0

        for metric, stats in actions.items():
            attempts = stats.get("attempts", 0)
            success = stats.get("success", 0)
            contrib = self._calc_action_contribution(metric, attempts, success)

            if metric.startswith("A_"):
                fai_attack += contrib
            else:
                fai_defense += contrib

        return {
            "fai_attack": round(fai_attack, 3),
            "fai_defense": round(fai_defense, 3),
            "fai_total": round(fai_attack + fai_defense, 3),
        }
