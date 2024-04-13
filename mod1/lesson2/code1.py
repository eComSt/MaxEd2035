login = "Max"
password = "123456!"

login_input  = input("Enter login:")
password_input  = input("Enter password:")

# if login == login_input and password ==password_input:
#     print("Access granded")

# if login == login_input:
#     print("Login corrrect")
# elif login=="Admin":
#     print("Login of admin")
# else:
#     print("Login incorrrect")

# if  password ==password_input:
#     print("Password corrrect")

age =  int(input())

if age > 65:
    print("Вы пенсионер")
elif age>25:
    print("Пора на работу")
elif age>16:
    print("Вы студент")
else:
    print("Вы молодец")