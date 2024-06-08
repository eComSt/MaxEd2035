ans = len(list(filter(lambda x: len(set(x))==len(x), input().split())))
print(ans)
