
import unittest
from funcs import *

# here is a sample puzzle for you to use in your tests
puzzle = ["WAhowTTWEE",
          "yBMIVQQELS",
          "uZXgKWIIIt",
          "mDWLaXPIPr",
          "PONDTnVAMa",
          "OEDSOYgGOf",
          "LGQCKGMMCT",
          "YCSLOACUZM",
          "XVDMGSXCYZ",
          "UUIUNIXFNU"]

class TestCases(unittest.TestCase):
   def test_check_right1(self):
      self.assertEqual(check_right('how', puzzle), (0,2,"FORWARD"))

   def test_check_right2(self):
      self.assertEqual(check_right('hoe', puzzle), -1)

   def test_check_left1(self):
      self.assertEqual(check_left('woh', puzzle), (0,4, "BACKWARD"))
   
   def test_check_left2(self):
      self.assertEqual(check_left('wop', puzzle), -1)

   def test_check_down1(self):
      self.assertEqual(check_down('yum', puzzle), (1,0, "DOWN"))

   def test_check_down2(self):
      self.assertEqual(check_down('yuk', puzzle), -1)

   def test_check_up1(self):
      self.assertEqual(check_up('fart', puzzle), (5,9, "UP"))

   def test_check_up2(self):
      self.assertEqual(check_up('fark', puzzle), -1)

   def test_check_diagonal1(self):
      self.assertEqual(check_diagonal('gang', puzzle), (2,3, "DIAGONAL"))
   def test_check_diagonal1(self):
      self.assertEqual(check_diagonal('gong', puzzle), -1)


   def test_new_puzzle1(self):
      new_puzzle = []
      new_puzzle.append('WyumPOLYXU')
      new_puzzle.append('ABZDOEGCVU')
      new_puzzle.append('hMXWNDQSDI')
      new_puzzle.append('oIgLDSCLMU')
      new_puzzle.append('wVKaTOKOGN')
      new_puzzle.append('TQWXnYGASI')
      new_puzzle.append('TQIPVgMCXX')
      new_puzzle.append('WEIIAGMUCF')
      new_puzzle.append('ELIPMOCZYN')
      new_puzzle.append('EStrafTMZU')
      self.assertEqual(reverse_puzzle(puzzle), new_puzzle)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

