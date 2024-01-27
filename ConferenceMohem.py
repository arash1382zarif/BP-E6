n = int(input())
emails = set()
for i in range(n):
    email = input()
    try:
        email = email[email.rindex("@")+1:]
    except:
        email = ""
    emails.add(email)

emails = sorted(emails)
for m in emails:
    print(m)