#dot
#import numpy as np
# A=np.arange(21,30).reshape(3,3)
# B=np.arange(31,40).reshape(3,3)
# print(A)
# print(B)
# c=A.dot(B)
# print(c)

#dot2
#ABC =  (AB)C = A(BC)

import numpy as np
A=np.arange(1,10).reshape(3,3)
B=np.arange(11,20).reshape(3,3)
C=np.arange(21,30).reshape(3,3)

temp1=(A.dot(B)).dot(C)
print(temp1)
temp2=(A.dot((B.dot(C))))
print(temp2)