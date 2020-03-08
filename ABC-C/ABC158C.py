def resolve():
    a, b = map(int, input().split())
    for i in range(10000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
    print(-1)

import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """2 2"""
        output = """25"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """8 10"""
        output = """100"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """19 99"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()