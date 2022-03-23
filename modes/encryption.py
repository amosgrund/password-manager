import getpass
import bcrypt
import keyring

def choosepw():
    while True:
        passwordfirst = getpass.getpass("Set your password:\n").encode()

        passwordrepeat = getpass.getpass("Repeat your password:\n").encode()

        if passwordfirst==passwordrepeat:
            password = passwordrepeat

            salt = bcrypt.gensalt(rounds=15)

            hashed = bcrypt.hashpw(password, salt).decode('utf-8')

            NAMESPACE = "masterhashed"

            ENTRY = "API_KEY"

            keyring.set_password(NAMESPACE, ENTRY, hashed)
            break
        else:
            print("Passwords don't match!")
            continue

def enterpw():
    while True:
        NAMESPACE = "masterhashed"

        ENTRY = "API_KEY"

        cred = keyring.get_password(NAMESPACE, ENTRY)

        getpassword = str(cred)

        password = getpass.getpass("Enter your password:\n").encode()

        if bcrypt.checkpw(password, (getpassword).encode()):
            print("Successfully logged in!")
            break
        else:
            print("Wrong password!")
            choice = input("Do you want to try again or quit? (retry/exit)\n")
            if choice == "retry":
                continue
            else:
                exit()