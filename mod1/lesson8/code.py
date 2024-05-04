# file = open("file.txt",mode = 'r', encoding='UTF-8')
# data = file.read()
# print(file)
# data = file.readline()
# print(data) 
# data = file.readline()
# print(data) 
# file.close()

# with open("file.txt",mode = 'r', encoding='UTF-8') as file:
#     data = file.read()
#     print(data)
# lst = []
# with open("file.txt",mode = 'r', encoding='UTF-8') as file:
#     for i in file:
#         num = int(i.strip())
#         lst.append(num)
# print(sum(lst),len(lst),max(lst),min(lst))

with open("file.txt",mode = 'a', encoding='UTF-8') as file:
    file.write("123\n")
    file.write("456\n")
    file.write("789\n")
    file.write("1000\n")