# a = [1, 22, 48, 16, "Bill"]
# B = ["Monday", True, "Test"]
# c = a + B

# print(c)
# print(type(c))

# c = tuple(c)
# print(c)
# print(type(c))

# print(c[-1])


# c = "Bill", 28, "admin"
# print(type(c))

# name, age, role = c

# print(name)
# print(age)
# print(role)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
 
 
# user = get_user()
# print(user[0])              # Tom
# print(user[1])              # 22
# print(user[2])              # False


telephones = [
    {"name": "Iphone",
     "model": "5",
     "price": 4000
    },
    {"name": "Iphone",
     "model": "5s",
     "price": 5000
    },
    {"name": "Iphone",
     "model": "6",
     "price": 6000
    },
    {"name": "Iphone",
     "model": "6s",
     "price": 7000
    },
    {"name": "Iphone",
     "model": "10",
     "price": 20000
    },
    {"name": "Samsung",
     "model": "S7",
     "price": 7000
    },
    {"name": "Samsung",
     "model": "S8",
     "price": 9000
    },
    {"name": "Samsung",
     "model": "S10",
     "price": 19000
    },
    {"name": "Xiomi",
     "model": "mi6",
     "price": 6000
    },
    {"name": "Xiomi",
     "model": "mi8",
     "price": 9000
    },
]
for item in telephones:
    print(item["name"], item["model"], item["price"], "\n", "◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘")

