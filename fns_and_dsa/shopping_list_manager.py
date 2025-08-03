#!/bin/bash/python3

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item = input("Enter item: ")
            shopping_list.append(add_item)
            print(f"'{add_item}' added to the list.")

        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Enter an item to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"'{remove_item}' removed from the list.")
            else:
                print(f"'{remove_item}' not found in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Current Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

