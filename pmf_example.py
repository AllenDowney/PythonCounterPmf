"""This file contains code examples I used for a talk.

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from collections import Counter
import myplot


class Pmf(Counter):
    """A Counter with probabilities."""

    def Normalize(self):
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

    def Render(self):
        """Returns values and their probabilities, suitable for plotting."""
        return zip(*sorted(self.items()))


d6 = Pmf([1,2,3,4,5,6])
d6.Normalize()
print d6
d6.name = 'one die'

d6_twice = d6 + d6
d6_twice.name = 'two dice'

for key, prob in d6_twice.items():
    print key, prob

pmf_ident = Pmf([0])
d6_thrice = sum([d6]*3, pmf_ident)
d6_thrice.name = 'three dice'

for key, prob in d6_thrice.items():
    print key, prob

myplot.PrePlot(3)
myplot.Pmf(d6)
myplot.Pmf(d6_twice)
myplot.Pmf(d6_thrice)
myplot.Save(root='pmf_example',
            xlabel='Total',
            ylabel='Probability')

