from time import time

class Ttime(object):
    def __init__(self):
        self.start = time()
    def __enter__(self):
        return self.start
    def __exit__(self, exc_type, exc_value, traceback):
        print(time()-self.start)


with Ttime():
    [i**5 for i in range(10_000_000)]