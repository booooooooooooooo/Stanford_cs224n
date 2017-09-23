
import numpy as np
import random

def getRandomContext(C):
      tokens = ["a", "b", "c", "d", "e"]
      return tokens[random.randint(0,4)], \
          [tokens[random.randint(0,4)] for i in xrange(2*C)]

if __name__ == "__main__":
    x = np.zeros([3,3])
    print x[1]
    print x[1].shape
    print x[1,:]
    print x[1,:].shape
