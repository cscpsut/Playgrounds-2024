from Crypto.Util.number import *
from secret import FLAG

f = bytes_to_long(FLAG)

def encrypt(m):
    return m * getPrime(1024)


def main():
    print("After the head shaving encryption scheme failed, Tutankhamun asked his vizier to come up with a new encryption scheme.")
    print("The vizier set up this challenge to test how resilient the new encryption scheme is.")
    print("If you can solve this challenge, Tutankhamun will award you with allowing you to leave with your life (:")
    
    while True:
        print("1. Encrypt")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(encrypt(f))
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

