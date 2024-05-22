student1 = ['litr','math','hist']
student2 = ['litr','math','phiz']
student3 = ['phiz','chem','obj','hist','litr']
student4 = ['phiz','chem','obj','hist','litr','math']
student5 = ['phiz','chem','obj','phy']
summary = student1 + student2 + student3 + student4 + student5
print(set(summary))

str1 = 'I love cats'
str2 = 'cats'
print(set(str2).issubset(str1))
print(set(str1).issuperset(str1))