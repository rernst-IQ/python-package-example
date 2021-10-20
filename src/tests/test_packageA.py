import unittest

from packageA import logic


class TestLogic(unittest.TestCase):
    def test_freezing(self):
        self.assertEqual(logic.complicated_logic(32), 0)

    def test_boiling(self):
        self.assertEqual(logic.complicated_logic(212), 100)
