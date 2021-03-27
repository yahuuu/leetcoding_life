import numpy as np

a=np.reshape(np.arange(6), (3, 2))
b=np.reshape(np.arange(10, 16), (3, 2))
a = np.expand_dims(a, axis=0)
b = np.expand_dims(b, axis=0)

print(a.shape)
print(b.shape)
for i in range(3):
    a = np.vstack((a, b))
print(a.shape)
print(a)
