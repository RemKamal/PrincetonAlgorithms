#!/usr/bin/env python

import unittest
from AlgsSedgewickWayne.Shell import *
from AlgsSedgewickWayne.ArrayHistory import *

class Selection_Tests(unittest.TestCase):

  def test_1(self):
    # (seed = 183182)
    # Give the array that results after the first 4 exchanges when
    # selection sorting the following array:
    desc = 'SHELL SORT'
    a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
    array_history = []
    Sort(a, array_history)
    print desc, "RESULT", a
    prt_array_history(array_history)
    show_array_history(desc, array_history)
    print

if __name__ == '__main__':
  unittest.main()


