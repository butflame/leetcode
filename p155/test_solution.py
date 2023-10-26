from unittest import TestCase

from .solution import MinStack


class Test(TestCase):
    def test_it(self):
        s = MinStack()
        assert s.push(-2) is None
        assert s.push(0) is None
        assert s.push(-3) is None
        assert s.getMin() == -3
        assert s.pop() is None
        assert s.top() == 0
        assert s.getMin() == -2
