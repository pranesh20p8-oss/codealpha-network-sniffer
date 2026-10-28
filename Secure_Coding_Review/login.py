
import os
import json
import hashlib
import hmac
import secrets
import getpass

USER_FILE = "users.json"
MAX_ATTEMPTS = 3


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        200000
    )


def create_account():
    username = input("Create username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    password = getpass.getpass("Create password: ")

    if len(password) < 8:
        print("Password must have at least 8 characters.")
        return

    salt = secrets.token_bytes(16)
    password_hash = hash_password(password, salt)

    users = {
        username: {
            "salt": salt.hex(),
            "password_hash": password_hash.hex()
        }
    }

    with open(USER_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file)

    print("Account created successfully!")


def login():
    if not os.path.exists(USER_FILE):
        print("No account found. Create an account first.")
        return

    with open(USER_FILE, "r", encoding="utf-8") as file:
        users = json.load(file)

    for attempt in range(MAX_ATTEMPTS):
        username = input("Enter username: ").strip()
        password = getpass.getpass("Enter password: ")

        user = users.get(username)

        if user:
            salt = bytes.fromhex(user["salt"])
            expected = bytes.fromhex(user["password_hash"])
            actual = hash_password(password, salt)

            if hmac.compare_digest(actual, expected):
                print("Login successful!")
                return

        print("Invalid username or password.")

    print("Maximum attempts reached. Try again later.")


print("1. Create account")
print("2. Login")

choice = input("Choose an option: ")

if choice == "1":
    create_account()
elif choice == "2":
    login()
else:
    print("Invalid choice.")
