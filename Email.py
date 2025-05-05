def validate_email(email):
    if '@' not in email or email.count('@') != 1:
        return False

    ename, domain = email.split('@')

    if not ename or not ename.isalnum():
        return False

    if '.' not in domain or domain.count('.') != 1:
        return False

    subdomain, extension = domain.split('.')
    if not subdomain or not extension:
        return False

    return True


email = input("Enter email: ")

while not validate_email(email):
    print("Invalid email")
    email = input("Enter email: ")

print("Valid email")
