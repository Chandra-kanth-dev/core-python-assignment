def add_item(menu, item):
    menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in menu")

def check_item(menu, item):
    return f"{item} is available" if item in menu else f"{item} not available"

if __name__ == "__main__":
    menu = input("Enter initial menu items (comma separated): ").split(",")
    menu = [m.strip() for m in menu]

    add_item(menu, input("Enter item to add: "))
    remove_item(menu, input("Enter item to remove: "))
    check = input("Enter item to check: ")

    print("Updated menu:", menu)
    print("Availability:", check_item(menu, check))
