import unittest
from tricubic import tricubic

class MainTest(unittest.TestCase):
    def test_constant(self):
        n = 4
        c = 1
        a = [[[c for k in range(n)] for j in range(n)] for i in range(n)]
        ip = tricubic(a, [n, n, n])
        for i in range(2*n):
            for j in range(2*n):
                for k in range(2*n):
                    v = ip.ip([0.5*i, 0.5*j, 0.5*k])
                    self.assertEqual(v, c)

    def test_linear_trivial(self):
        f = lambda x, y, z : (x + 1.2) + (0.2 * y - 0.1) + z * 4
        n = 5
        a = [[[f(i, j, k) for k in range(n)] for j in range(n)] for i in range(n)]
        ip = tricubic(a, [n, n, n])
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    v = ip.ip([i, j, k])
                    fv = f(i, j, k)
                    self.assertEqual(v, fv)

    def test_linear(self):
        f = lambda x, y, z : (x + 1.2) + (0.2 * y - 0.1) + z * 4
        n = 5
        a = [[[f(i, j, k) for k in range(n)] for j in range(n)] for i in range(n)]
        ip = tricubic(a, [n, n, n])
        x = 1.6; y = 2.3; z = 3.7
        v = ip.ip([x, y, z])
        self.assertEqual(v, 19.43)

if __name__ == '__main__':
    unittest.main()