stack = []

def is_empty():
    return len(stack) == 0

def push(item):
    stack.append(item)
    print(f"Pushed {item} onto the stack.")

def pop():
    if not is_empty():
        popped_item = stack.pop()
        print(f"Popped {popped_item} from the stack.")
        return popped_item
    else:
        print("Stack is empty")

def peek():
    if not is_empty():
        return stack[-1]
    else:
        print("Stack is empty")

def size():
    return len(stack)

def display():
    print(stack)

def display_menu():
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Display")
    print("6. Quit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            item = input("Enter item to push onto the stack: ")
            push(item)
        elif choice == "2":
            pop()
        elif choice == "3":
            top_item = peek()
            print(f"Top of the stack: {top_item}")
        elif choice == "4":
            print(f"Stack size: {size()}")
        elif choice == "5":
            display() 
        elif choice == "6":
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

