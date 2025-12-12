import argparse
from pwned_api import get_pwned_count

def main():
    parser = argparse.ArgumentParser(description="Check if a password appears in known breaches (HIBP).")
    parser.add_argument("password", nargs="?", help="Password to check. If omitted, will prompt securely.")
    args = parser.parse_args()

    if args.password:
        pwd = args.password
    else:
        import getpass
        pwd = getpass.getpass("Enter password to check (won't be shown): ")

    try:
        count = get_pwned_count(pwd)
    except Exception as e:
        print("Error:", e)
        return

    if count:
        print(f"🔒 This password was seen {count} times in breaches — change it!")
    else:
        print("✅ No matches found in the Pwned Passwords dataset.")

if __name__ == "__main__":
    main()
