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

if __name__ == "__main__":
    start()

def start(items):
    db_items = items

    exit = False
    while not exit:
        print("==========Sales Manager v0.1.28=========")
        choice = int(input("1. Add item \n2. Delete item \n3. Sort by price \n4. Sell item + sell score \n5. Sell statistics \n6. Show items \n0. Exit \n"))
        print("User choice =>", choice)
        if choice == 1:
            add_item(db_items)
        elif choice == 2:
            show_items(db_items)
        elif choice == 3:
            show_items(db_items)
        elif choice == 4:
            show_items(db_items)
        elif choice == 5:
            show_items(db_items)
        elif choice == 6:
            show_items(db_items)
        elif choice == 0:
            exit = True
        else:
            print("Read menu and check N !!!")


def show_items(items):
    print(items)


def add_item(items):
    
    name = input("Enter name phone :")
    model = input("Enter model phone :")
    price = int(input("Enter price phone :"))
    item = {"name": name,
            "model": model,
            "price": price
            }
    items.append(item)        
            