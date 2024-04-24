# res = []
# for _ in range(5):
#     res.append(int(input())**2)
# print(sorted(res,reverse=True))

# res.sort(reverse=True)
# res_sortes = sorted(res,reverse=True)
# print(res)

# res = [int(input())**2 for _ in range(5)]
print(sorted([int(input())**2 for _ in range(5)],reverse=True))

# lst = [1,3,2,5,7,12]
# print(lst[-1])