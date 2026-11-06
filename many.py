import string
import secrets

def password_checker():
    password = input("Enter sample password: ")

    score = 0
    score += len(password) >= 8
    score += any(c.islower() for c in password)
    score += any(c.isupper() for c in password)
    score += any(c.isdigit() for c in password)
    score += any(c in string.punctuation for c in password)

    level = "WEAK" if score <= 2 else (
        "MEDIUM" if score <= 3 else "STRONG"
    )

    print("\n--- CYBERYKS SECURITY REPORT ---")
    print("Strength:", level)
    print("Score:", score, "/ 5")


def password_generator():
    length = 16
    chars = string.ascii_letters + string.digits + "!@#$%"
    password = "".join(
        secrets.choice(chars) for _ in range(length)
    )
    print("Generated password:", password)


def main():
    while True:
        print("\n===== CYBERYKS =====")
        print("1. Password Checker")
        print("2. Password Generator")
        print("3. Exit")

        choice = input("Select: ")

        if choice == "1":
            password_checker()
        elif choice == "2":
            password_generator()
        elif choice == "3":
            print("CyberYKS Closed")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
