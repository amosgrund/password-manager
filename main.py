
#password manager main
#profiles service emailuser passwd

from modes import enterpw
import time

def main():
    enterpw()

    print("Add, view or delete a profile. Type 'exit' if you want to quit: (add/view/delete/exit)")

    while True:

        choice = input()

        if choice == "add":
            from modes import add
            add()
            print("Add, view or delete another profile. Type 'exit' if you want to quit: (add/view/delete/exit)")
        elif choice == "view":
            from modes import view
            view()
            print("Add, view or delete another profile. Type 'exit' if you want to quit: (add/view/delete/exit)")
        elif choice == "delete":
            from modes import delete
            delete()
            print("Add, view or delete another profile. Type 'exit' if you want to quit: (add/view/delete/exit)")
        elif choice == "exit":
            print("See you next time!")
            time.sleep(3)
            exit()
        else:
            print("That's not a valid input. Try again:")
            continue

if __name__ == "__main__":
    main()