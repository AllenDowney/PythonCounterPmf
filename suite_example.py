"""This file contains code examples I used for a talk.

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from collections import Counter


class Pmf(Counter):
    """A Counter with probabilities."""

    def normalize(self):
        """Normalizes the PMF so the probabilities add to 1."""
        total = float(sum(self.values()))
        for key in self:
            self[key] /= total

    def __add__(self, other):
        """Adds two distributions.

        The result is the distribution of sums of values from the
        two distributions.

        other: Pmf

        returns: new Pmf
        """
        pmf = Pmf()
        for key1, prob1 in self.items():
            for key2, prob2 in other.items():
                pmf[key1 + key2] += prob1 * prob2
        return pmf

    def __hash__(self):
        return id(self)

    def render(self):
        """Returns values and their probabilities, suitable for plotting."""
        return zip(*sorted(self.items()))


class Suite(Pmf):
    """Map from hypothesis to probability."""

    def update(self, data):
        """
        """
        for hypo in self:
            like = self.Likelihood(data, hypo)
            self[hypo] *= like

        self.normalize()


class DiceSuite(Suite):
    
    def likelihood(self, data, hypo):
        return hypo[data]
        

def make_die(num_sides):
    die = Pmf(range(1, num_sides+1))
    die.name = 'd%d' % num_sides
    die.normalize()
    return die


dice = [make_die(x) for x in [4, 6, 8, 12, 20]]

metapmf = DiceSuite(dice)
metapmf.update(6)

for die, prob in sorted(metapmf.items()):
    print die.name, prob

