
import numpy as np
import random

def getRandomContext(C):
      tokens = ["a", "b", "c", "d", "e"]
      return tokens[random.randint(0,4)], \
          [tokens[random.randint(0,4)] for i in xrange(2*C)]

if __name__ == "__main__":
    # print getRandomContext(5)
    # indices = [1]
    # indices.extend([2,3,4,5,6])
    # for i in xrange(1,len(indices) ):
    #     print i
    y = np.zeros([1,1])
    x = np.log(y[0,0])
    print x
    x = np.log([1])

    print x
    x = np.log(1)
    print x
