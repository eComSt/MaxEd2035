n = int(input())
result = set()
for i in range(n):
    result.add(i+1)
while True:
    ask = input()
    if ask == 'HELP':
        print(result)
        break
    else:
        ask = ask.split()
        for i in range(len(ask)):
            ask[i] = int(ask[i])
        ask = set(ask)
    answear = input()
    if answear == 'YES':
        result = result.intersection(ask)
    else:
        result = result.difference(ask)
