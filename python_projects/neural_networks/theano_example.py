#!usr/bin/env python

import numpy
import theano.tensor as T
from theano import function

x = T.dmatrix('x')
y = T.dmatrix('y')
z = x + y
f = function([x, y], z)

print f(2, 3)

