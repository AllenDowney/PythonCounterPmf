"""This file contains code examples I used for a talk.

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import suite

class DiceSuite(suite.Suite):
    
    def likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        data: result of a die roll
        hypo: Die object
        """
        return hypo[data]
        

def make_die(num_sides):
    die = suite.Pmf(range(1, num_sides+1))
    die.name = 'd%d' % num_sides
    die.normalize()
    return die


dice = [make_die(x) for x in [4, 6, 8, 12, 20]]
dice_suite = DiceSuite(dice)

dice_suite.bayesian_update(6)


for die, prob in sorted(dice_suite.items()):
    print die.name, prob

