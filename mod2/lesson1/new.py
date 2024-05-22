from time import time
lst = [i for i in range(1000)]
st = set()
for i in lst:
    st.add(i)
x = 998
t = time()
x in lst
print(time() - t)
t = time()
x in st
print(time() - t)