import numpy as np

import optuna


def test_exact_2d() -> None:
    for n in range(2, 20):
        r = n * np.ones(2)
        s = np.asarray([[n - 1 - i, i] for i in range(n)])
        for i in range(n + 1):
            s = np.vstack((s, np.asarray([i, n - i])))
        v = optuna.multi_objective.hypervolume.Exact2d().compute(s, r)
        assert v == n * n - n * (n - 1) // 2
