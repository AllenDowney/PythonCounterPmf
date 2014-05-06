"""This file contains code examples I used for a talk.

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import suite
import matplotlib.pyplot as pyplot

d6 = suite.Pmf([1,2,3,4,5,6])
d6.normalize()
print d6
d6.name = 'one die'

d6_twice = d6 + d6
d6_twice.name = 'two dice'

for key, prob in d6_twice.items():
    print key, prob

pmf_ident = suite.Pmf([0])
d6_thrice = sum([d6]*3, pmf_ident)
d6_thrice.name = 'three dice'

for key, prob in d6_thrice.items():
    print key, prob

for die in [d6, d6_twice, d6_thrice]:
    xs, ys = die.render()
    pyplot.plot(xs, ys, label=die.name, linewidth=2, alpha=0.5)
    
pyplot.xlabel('Total')
pyplot.ylabel('Probability')
pyplot.legend()
pyplot.show()

