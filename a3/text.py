import tensorflow as tf
sess = tf.Session()

a = [1,2,3]
b = {'a' : 1, 'b' : 2, 'c' : 3}
c = ['a', 'b', 'c']
d = [('a', 1), ('b', 2), ('c', 3)]

k, v = zip(*d)
print k
print v
print zip(k, v)
