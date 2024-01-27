#!/usr/bin/env python3
# Author: Arash Zarif

def extract_domain(email):
    """Extract domain from email."""
    try:
        return email[email.rindex("@") + 1:]
    except ValueError:
        return ""


def main():
    n = int(input())
    unique_domains = set()

    for _ in range(n):
        email = input()
        domain = extract_domain(email)
        unique_domains.add(domain)

    sorted_domains = sorted(unique_domains)
    for domain in sorted_domains:
        print(domain)


if __name__ == "__main__":
    main()
