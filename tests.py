import numpy as np
from pac import *
import unittest

class TestNoiseDetermination(unittest.TestCase):
    def setUp(self):
        #define mechanism to be tested. in this case, this is the polynomial basis
        self.M = M

    def test_code_runs(self):
        #distribution + parameters all defined in pac module
        Sigma_B = noise_determination(self.M, distrib, m, c, v, beta, r, d)

        #assert output is positive definite
        self.assertTrue(np.all(np.linalg.eigvals(Sigma_B) > 0))
        #define baseline
        self.baseline = np.mean(Sigma_B[i][i] for i in range(len(Sigma_B)))

    def test_code_correctness_with_lower_bound(self):
        c = 0.001
        beta = 0.001
        v = 0.001
        Sigma_B = noise_determination(self.M, distrib, m, c, v, beta, r, d)

        #avg noise > baseline noise because we've decreased the upper bound on MI
        avg = np.mean(Sigma_B[i][i] for i in range(len(Sigma_B)))
        self.assertTrue(avg > self.baseline)

    def test_code_correctness_with_higher_bound(self):
        c = 0.3
        beta = 0.3
        v = 0.3
        Sigma_B = noise_determination(self.M, distrib, m, c, v, beta, r, d)

        #avg noise < baseline noise because we've increased the upper bound on MI
        avg = np.mean(Sigma_B[i][i] for i in range(len(Sigma_B)))
        self.assertTrue(avg < self.baseline)
    
if __name__ == '__main__':
    unittest.main()
