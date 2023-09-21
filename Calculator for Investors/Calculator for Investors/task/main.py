def show_menu():

    try:
        choice = int(input("""MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria\n\nEnter an option:\n"""))
        # type(choice) == int
    except ValueError:
        print("Invalid option!\n")
        return show_menu()
    return choice


def crud_menu():
    try:
        choice = int(input("""\nCRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies\n\nEnter an option:\n"""))
    except ValueError:
        print("Invalid option!\n")
        return show_menu()
    return choice


def top_ten():
    try:
        choice = int(input("""\nTOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA\n\nEnter an option:\n"""))
    except ValueError:
        print("Invalid option!\n")
        return show_menu()
    return choice


def main_func():
    while True:
        x = show_menu()
        if x == 0:
            print("Have a nice day!")
            break
        elif x == 1:
            y = crud_menu()
            if y in [1, 2, 3, 4, 5]:
                print("Not implemented!\n")
        elif x == 2:
            z = top_ten()
            if z in [1, 2, 3]:
                print("Not implemented!\n")
        else:
            print("Invalid option!\n")


if __name__ == '__main__':
    main_func()