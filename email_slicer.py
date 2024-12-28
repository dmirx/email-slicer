
print("Hello this will be an email slicer")
print("==================================")

while True:
    email = input("Enter your whole email (e.g: email@domain.com): ").strip()

    if email.count("@") == 1:
        try:
            username = email[:email.index('@')]
            domain = email[email.index('@') + 1:]

            if username and domain:
                    print(f"Your email is {username} and your domain is {domain}")
            elif not username:
                print("Missing username in email")
            elif not domain:
                print("Missing domain name in email")
        except ValueError:
            print("Invalid email format")
    else:
        print("Please ensure there is exactly one '@' in the email")

    continue_email = input("Would you like to enter another email (y/n): ").strip().lower()
    if continue_email in ["y", "yes"]:
        continue
    elif continue_email in ["n", "no"]:
        print("Goodbye")
        break
    else:
        print("Please enter 'y' or 'yes' for yes, or 'n' or 'no' for no.")