import time

start = time.perf_counter()
for i in range(100000000):
    pass
t = time.perf_counter() - start
print("t={}s".format(t))