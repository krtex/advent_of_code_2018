import numpy as np

test1 = np.zeros((2,2))
result1 = np.array([(0,0),(0,1)])

test2 = np.zeros((5,5))
result2 = np.array([(0,0,0,0,0), \
                    (0,1,1,0,0), \
                    (0,1,2,1,0), \
                    (0,0,1,1,0), \
                    (0,0,0,0,0)])


#print(test1, result1, test1+result1)

block = np.ones((2,2))
position = (1,1)
x, y = position
a, b = block.shape
print(x,y,a,b)
test2[x:x+a, y:y+b] += 1

print(test2)

print(np.sum(test2[1:3,1:3]))
