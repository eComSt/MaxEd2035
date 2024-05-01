# a = 12
# exit = True
# while exit:
#     b = int(input())
#     if b == 0:
#         break
#     else:
#         if a>b:
#             print("My value is greater than yours")
#         elif a<b:   
#             print("My value is less than yours")
#         else:
#             print("Cool")
#             exit = False
# else:
#     print("I am done with the loop")

dct = {
    0:"value0",
    "key":"value",
    "key2":"value",
    }
print(dct['key'])
print(dct.get('key3','default'))