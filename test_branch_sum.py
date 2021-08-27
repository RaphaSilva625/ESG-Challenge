import unittest
#importing the function that i want to test.
from esg_challenge import branch_sum

#Creating a test function.
class BranchSum(unittest.TestCase):

    def test_branch_sum(self):
        self.assertEqual(2130621.4800000037, branch_sum('01'))


if __name__ == '__main__':
    unittest.main()