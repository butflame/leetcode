from unittest import TestCase

from .solution import RandomizedSet


class Test(TestCase):
    def test_it(self):
        rs = RandomizedSet()
        rs.insert(1)
        rs.remove(2)
        rs.insert(2)
        rs.getRandom()
        rs.remove(1)
        rs.insert(2)
        rs.getRandom()
